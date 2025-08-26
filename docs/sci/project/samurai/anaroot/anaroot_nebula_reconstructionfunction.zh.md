```c++
void TArtCalibNEBULA::ReconstructData()
{
  if(!fDataLoaded) LoadData();
  //共通のoffset。どう値を取ってくるかは後で考える(とりあえず手打ち？)。
  Double_t posxoff = 0;
  Double_t posyoff = 0;
  Double_t poszoff = 0;
  for(Int_t i=0;i<GetNumNEBULAPla();++i){
    TArtNEBULAPla* pla = GetNEBULAPla(i);
    Int_t id = pla->GetID();
    const TArtNEBULAPlaPara* para = FindNEBULAPlaPara(id);
    if(!para){
      TArtCore::Info(__FILE__,"cannot find para %d", id); // programming problem
      continue;
    }
    if (para->IsTref()) continue;
    // find tref
    TArtRIDFMap map_u = para->GetMapTU();
    TArtRIDFMap map_d = para->GetMapTD();
    Double_t turaw_ref = GetTRef(map_u);
    Double_t tdraw_ref = GetTRef(map_d);
//    std::cout<<id<<" "
//	     <<"TU="<<pla->GetTURaw()<<" "
//	     <<"TU_tl="<<pla->GetTURaw_Trailing()<<" "
//	     <<"QU="<<pla->GetQURaw()<<" "
//	     <<"tref_u="<<turaw_ref<<"    "
//	     <<"TD="<<pla->GetTDRaw()<<" "
//	     <<"TD_tl="<<pla->GetTDRaw_Trailing()<<" "
//	     <<"QD="<<pla->GetQDRaw()<<" "
//	     <<"tref_d="<<tdraw_ref<<" "
//	     <<std::endl;
    Double_t turaw = pla->GetTURaw();
    Double_t tdraw = pla->GetTDRaw();
    Double_t turaw_subtref = turaw - turaw_ref;
    Double_t tdraw_subtref = tdraw - tdraw_ref;
    Double_t turaw_width = pla->GetTURaw_Trailing() - pla->GetTURaw();
    Double_t tdraw_width = pla->GetTDRaw_Trailing() - pla->GetTDRaw();
    Double_t quraw = pla->GetQURaw();
    Double_t qdraw = pla->GetQDRaw();
    double t0 = TArtMath::InvalidNum();
    if(fT0Array){
      if(0 == fT0Array->GetEntries()){
    TArtCore::Error(__FILE__,"CalibSAMURAIT0 seems not to be reconstructed.\n Cannot reconstruct CalibSAMURAITZero.");
      }else{
    //	t0 = ((TArtTZero*)fT0Array->At(0))->GetTZeroCal();
    t0 = ((TArtTZero*)fT0Array->At(0))->GetTZeroSlw();
      }
    }
    Int_t hit = 0;
    if(TMath::Finite(quraw)) hit += 1;
    if(TMath::Finite(qdraw)) hit += 2;
    if(TMath::Finite(turaw)) hit += 4;
    if(TMath::Finite(tdraw)) hit += 8;      
    Double_t quped = quraw - para->GetQUPed();
    Double_t qdped = qdraw - para->GetQDPed();
    Double_t qucal = quped * para->GetQUCal();
    Double_t qdcal = qdped * para->GetQDCal();
    Double_t qaveped = sqrt(quped*qdped);
    Double_t qavecal = para->GetQAveCal()*sqrt(qucal*qdcal);
    Double_t logqped = log(quped/qdped);
    Double_t logqcal = log(qucal/qdcal);
    Double_t ivsqrtquped = 1/sqrt(quped);
    Double_t ivsqrtqdped = 1/sqrt(qdped);
    Double_t ivsqrtqaveped = 1/sqrt(qaveped);
    Double_t tucal = turaw_subtref * para->GetTUCal() + para->GetTUOff();
    Double_t tdcal = tdraw_subtref * para->GetTDCal() + para->GetTDOff();
    Double_t tucal_width = turaw_width * para->GetTUCal();
    Double_t tdcal_width = tdraw_width * para->GetTDCal();
    Double_t tuslw = tucal;
    Double_t tdslw = tdcal;
    if(para->GetTUSlwLog(0) != 0 && para->GetTDSlwLog(0) != 0){
      double logquped = log(quped);
      double logqdped = log(qdped);
      double logquped2 = logquped*logquped;
      double logqdped2 = logqdped*logqdped;
      double logquped4 = logquped2*logquped2;
      double logqdped4 = logqdped2*logqdped2;
      tuslw -= (para->GetTUSlwLog(0)*logquped +
        para->GetTUSlwLog(1)*logquped2 +
        para->GetTUSlwLog(2)*logquped2*logquped +
        para->GetTUSlwLog(3)*logquped4 +
        para->GetTUSlwLog(4)*logquped4*logquped);
      tdslw -= (para->GetTDSlwLog(0)*logqdped +
        para->GetTDSlwLog(1)*logqdped2 +
        para->GetTDSlwLog(2)*logqdped2*logqdped +
        para->GetTDSlwLog(3)*logqdped4 +
        para->GetTDSlwLog(4)*logqdped4*logqdped);
    }else{
      tuslw -= para->GetTUSlw()/sqrt(quped);
      tdslw -= para->GetTDSlw()/sqrt(qdped);
    }
    Double_t dtraw = tdraw - turaw;
    Double_t dtcal = tdcal - tucal;
    Double_t dtslw = tdslw - tuslw;
    Double_t taveraw = (turaw_subtref + tdraw_subtref)/2.;
    Double_t tavecal = (tucal + tdcal)/2 + para->GetTAveOff();
    Double_t taveslw = (tuslw + tdslw)/2 + para->GetTAveOff();
    Double_t poscal = dtcal * para->GetDTCal() + para->GetDTOff();
    Double_t posslw = dtslw * para->GetDTCal() + para->GetDTOff();
    
    Double_t tucalt0 = tucal - t0;
    Double_t tdcalt0 = tdcal - t0;
    Double_t tuslwt0 = tuslw - t0;
    Double_t tdslwt0 = tdslw - t0;
    Double_t tavecalt0 = tavecal - t0;
    Double_t taveslwt0 = taveslw - t0;
    Double_t pos[3];
    if(para->GetSubLayer() != 0){ // NEUT
      //      pos[0] = para->GetDetPos(0) + posxoff + gRandom->Uniform(-6,6);
      pos[0] = para->GetDetPos(0) + posxoff;
    }else{ // VETO
      //      pos[0] = para->GetDetPos(0) + posxoff + gRandom->Uniform(-16,16);
      pos[0] = para->GetDetPos(0) + posxoff;
    }
    pos[1] = posslw + para->GetDetPos(1) + posyoff; 
    pos[2] = para->GetDetPos(2) + poszoff;
    qavecal /= 1+pos[1]*pos[1]*para->GetQAveCalAtt();
    Double_t flightlength = sqrt(pos[0]*pos[0]+pos[1]*pos[1]+pos[2]*pos[2]);
    Double_t flightangle = sqrt(pos[0]*pos[0]+pos[1]*pos[1])/pos[2];
    Double_t ttofgamma = taveslw - flightlength/29.979; //beta=1
    Double_t ttofneutron = taveslw - flightlength/20.; //とりあえずbeta=2/3. 上流でのbetaを本当は取ってきたい。
    pla->SetHit(hit);
    pla->SetQUPed(quped);
    pla->SetQDPed(qdped);
    pla->SetQUCal(qucal);
    pla->SetQDCal(qdcal);
    pla->SetQAvePed(qaveped);
    pla->SetQAveCal(qavecal);
    pla->SetLogQPed(logqped);
    pla->SetLogQCal(logqcal);
    pla->SetIvSqrtQUPed(ivsqrtquped);
    pla->SetIvSqrtQDPed(ivsqrtqdped);
    pla->SetIvSqrtQAvePed(ivsqrtqaveped);
    pla->SetTURawRef(turaw_ref);
    pla->SetTDRawRef(tdraw_ref);
    pla->SetTURaw_SubTRef(turaw_subtref);
    pla->SetTDRaw_SubTRef(tdraw_subtref);
    pla->SetTURaw_Width(turaw_width);
    pla->SetTDRaw_Width(tdraw_width);
    pla->SetTUCal(tucal);
    pla->SetTDCal(tdcal);
    pla->SetTUCal_Width(tucal_width);
    pla->SetTDCal_Width(tdcal_width);
    pla->SetTUSlw(tuslw);
    pla->SetTDSlw(tdslw);
    pla->SetDTRaw(dtraw);
    pla->SetDTCal(dtcal);
    pla->SetDTSlw(dtslw);    
    pla->SetTAveRaw(taveraw);
    pla->SetTAveCal(tavecal);
    pla->SetTAveSlw(taveslw);    
    pla->SetTUCalT0(tucalt0);
    pla->SetTDCalT0(tdcalt0);
    pla->SetTUSlwT0(tuslwt0);
    pla->SetTDSlwT0(tdslwt0);
    pla->SetTAveCalT0(tavecalt0);
    pla->SetTAveSlwT0(taveslwt0);    
    pla->SetTTOFGamma(ttofgamma);
    pla->SetTTOFNeutron(ttofneutron);
    pla->SetPosCal(poscal);
    pla->SetPosSlw(posslw);
    pla->SetPos(pos);
    pla->SetFlightLength(flightlength);
    pla->SetFlightAngle(flightangle);
    pla->SetDataState(1);
  }
  
  fReconstructed = true;
}
```

这段代码实现了 TArtCalibNEBULA::ReconstructData() 方法，其主要功能是对 NEBULA 探测器的每个塑料闪烁体（Pla）探测单元进行物理量的重建和校准。

首先，函数会检查原始数据是否已加载（fDataLoaded），如果没有则调用 LoadData() 进行加载。接着定义了三个位置偏移量（posxoff、posyoff、poszoff），目前都设为 0，后续可根据实验需求调整。

主循环遍历所有 NEBULA 探测单元（通过 GetNumNEBULAPla() 和 GetNEBULAPla(i) 获取）。对于每个单元，先通过 ID 查找其参数对象 para，如果找不到参数则跳过。若该单元为参考信号（Tref），也直接跳过。

随后，代码获取上端（U）和下端（D）信号的参考时间（tref），并计算原始时间、宽度、能量等原始物理量。还会尝试获取全局 T0 校准（如有），用于后续时间修正。

接下来，代码根据原始能量和时间信号的有效性，计算命中类型（hit），并对能量信号进行扣除本底、校准、对数变换等多种处理，得到多种能量相关变量。时间信号也会经过参考时间校正、线性校准、slewing 校正（非线性校正，依赖能量），并计算时间差、平均时间等。

位置的重建基于时间差和参数表中的几何信息，最终得到三维空间坐标。还会根据位置和能量修正光衰减效应。最后，计算飞行长度、角度、以及针对不同粒子的飞行时间（TOF），如光子（gamma）和中子（neutron）。

所有计算结果通过一系列 Set 方法写回到 TArtNEBULAPla 对象中，标记数据已重建。循环结束后，设置 fReconstructed 标志为 true，表示本事件的所有探测单元数据已完成重建。

整体来看，这个方法实现了从原始信号到物理量（能量、时间、位置、TOF等）的完整重建流程，是 NEBULA 探测器数据分析的核心步骤。