# **揭秘面向对象编程：Geant4工具包深度导览**

## **第一部分：Geant4面向对象编程的核心原则**

### **1.1 引言：从“大一统”代码到对象世界**

Geant4（GEometry ANd Tracking的缩写）是一个用于模拟粒子在物质中传输的蒙特卡洛平台 [1](#ref-1)。作为其前身GEANT系列的继承者，Geant4做出了一个革命性的技术抉择：它是该系列中第一个完全采用面向对象编程（Object-Oriented Programming, OOP）思想，并使用C++语言实现的工具包 [1](#ref-1)。这一转变并非偶然，而是为了应对粒子物理模拟中日益增长的复杂性。一个完整的模拟需要精确地处理几何构建、粒子追踪、物理过程、探测器响应和数据管理等多个高度关联的领域 [2](#ref-2)。

为了更直观地理解这一转变的意义，我们可以做一个类比。假设任务是建造一辆精密的汽车。传统的“过程式编程”方法，就像是从一整块巨大的金属开始，一点点雕刻掉所有“不是汽车”的部分。整个过程高度耦合，牵一发而动全身，修改任何一个细节都可能导致意想不到的连锁反应。而面向对象编程则完全不同，它更像是组建一支由发动机专家、底盘设计师、车轮制造商等组成的专业团队。每个团队负责设计和制造一个独立的、功能完备的组件（一个发动机“对象”、一个车轮“对象”）。这些组件内部结构复杂，但对外只提供简单的接口（如油门、刹车、方向盘）。它们各自知道如何完成自己的工作，也知道如何与其他组件协同合作。Geant4正是以后者的方式构建的，它由无数个这样的“智能乐高积木”（即对象）组成，这些积木易于设计、测试、扩展和复用。

这种模块化、可扩展的强大能力，建立在面向对象编程的四大核心原则之上：封装（Encapsulation）、继承（Inheritance）、组合（Composition）以及多态（Polymorphism）与抽象（Abstraction）。这些原则并非空洞的理论，它们是Geant4能够成为一个灵活的“工具包”（toolkit）而非一个僵化程序的基石 [4](#ref-4)。接下来的章节将逐一剖析这些原则，并展示它们在Geant4中的具体应用。

### **1.2 封装：“黑箱”的艺术**

封装是面向对象编程的基础。它指的是将数据（属性）和操作这些数据的方法（函数）捆绑到一个称为“对象”的独立单元中。同时，对象会隐藏其内部的复杂实现细节，只对外暴露一个定义明确的公共接口（public methods），从而保护其内部数据不被外界随意篡改。这就像一个“黑箱”，用户知道它的功能和如何使用它，但无需关心其内部是如何工作的。

在Geant4中，G4Box类是封装原则的绝佳范例。当用户需要创建一个长方体时，他们只需在构造函数中提供其名称和三个方向的半长：new G4Box("aBoxSolid", 1.*m, 2.*m, 3.*m) [7](#ref-7)。

* **数据隐藏**：用户并不知道，也完全不需要知道，这三个半长在G4Box对象内部是如何存储的（例如，它们可能被存储为名为fDx, fDy, fDz的内部变量 [7](#ref-7)）。这就是“黑箱”原则的体现。  
* **公共接口**：如果用户想获取这个长方体的信息，他们必须通过调用公共的“getter”方法，如GetXHalfLength()来获取X方向的半长，或GetCubicVolume()来获取其体积 [7](#ref-7)。用户无法直接访问或修改内部的fDx变量。这种机制有效地防止了用户犯错，例如，用户无法将一个长度设置为负值，因为没有公共方法允许这样做。更进一步，G4Box的构造函数自身就包含了检查逻辑，如果用户提供的尺寸过小，它会抛出一个异常，从创建之初就保证了对象的有效性和物理世界的合理性 [7](#ref-7)。

这种设计带来的好处是深远的。封装是Geant4确保代码健壮性和可维护性的关键策略。通过强制用户通过公共API进行交互，Geant4的开发者可以自由地修改一个类的内部实现（例如，为了优化体积计算的算法），只要保持公共方法的名称和参数不变，用户的代码就完全不受影响。对于一个需要支持长达数十年科学实验的软件工具包而言，这种向后兼容性和稳定性至关重要 [3](#ref-3)。

### **1.3 继承：“是一个”的关系**

继承允许一个新类（称为“派生类”或“子类”）基于一个已有的类（称为“基类”或“父类”）来创建。子类会自动获得父类的所有公共和受保护的成员（数据和方法），这不仅实现了代码的复用，更重要的是能够建立起符合逻辑的类层次结构。这种关系通常被描述为“是一个”（Is-A）的关系。

Geant4的几何系统完美地诠释了继承的应用。

* G4VSolid是一个“抽象基类”，代表了所有几何形状的“始祖” [11](#ref-11)。它定义了一套所有“实体”都必须遵守的通用接口，例如，它声明了像Inside()（判断一个点是否在实体内部）、DistanceToIn()（计算从外部一个点到实体表面的距离）等函数，但它自己不提供具体的实现 [11](#ref-11)。  
* G4CSGSolid（构造实体几何）继承自G4VSolid [10](#ref-10)。它代表了由基本形状（如长方体、球体）通过布尔运算（并、交、差）组合而成的实体。  
* G4Box（长方体）则继承自G4CSGSolid [10](#ref-10)。

因此，一个G4Box对象**是一个**G4CSGSolid，而一个G4CSGSolid也**是一个**G4VSolid。这意味着，在任何需要一个指向G4VSolid对象的指针的地方，我们都可以安全地传入一个指向G4Box对象的指针。

继承机制是Geant4追踪系统能够做到通用化的核心。追踪算法在计算粒子下一步将运动到哪里时，它不需要关心当前面对的是一个G4Box、一个G4Tubs（圆柱体），还是一个复杂的G4UnionSolid（组合体）。它只需要知道自己持有一个G4VSolid类型的指针，因此可以放心地调用该指针的DistanceToIn()方法。C++的虚函数机制会确保在运行时自动调用指针所指向的真实对象类型（无论是G4Box还是G4Tubs）的那个特定版本的DistanceToIn()方法。这就是继承与多态相结合所产生的巨大威力。

### **1.4 组合：“有一个”的关系**

组合是另一种构建复杂对象的方式，它通过将其他对象作为自己的成员变量来实现。这种关系代表了“有一个”（Has-A）或“是...的一部分”（Part-of）的联系。例如，一个汽车对象可以由四个车轮对象和一个发动机对象**组合**而成。

在Geant4中，G4LogicalVolume（逻辑体）是体现组合关系的最重要典范。一个逻辑体代表了空间中一块具有特定物理属性的区域。

* 它的构造函数清晰地展示了这种关系：G4LogicalVolume(G4VSolid* pSolid, G4Material* pMaterial,...) [12](#ref-12)。  
* 这意味着，一个G4LogicalVolume**有一个**G4VSolid对象，用来定义它的形状和尺寸。  
* 它也**有一个**G4Material对象，用来定义它是由什么材料构成的 [9](#ref-9)。  
* 除此之外，它还可以拥有一个G4VSensitiveDetector（灵敏探测器）、一个G4FieldManager（场管理器）以及一个包含其所有子物理体的列表 [12](#ref-12)。G4LogicalVolume将所有这些不同的属性聚合在一个概念单元中。

与继承相比，组合提供了更大的灵活性。一个G4LogicalVolume并不是一种材料，也不是一种形状；它是一个独立的、更高层次的概念，它**使用**了形状和材料这两个对象。这种设计实现了“关注点分离”：G4VSolid及其子类家族只关心几何计算；G4Material类只关心物质的宏观物理属性；而G4LogicalVolume则负责将它们有机地结合成一个在模拟中可以被追踪的区域。如果当初的设计者错误地使用了继承（例如，让G4LogicalVolume继承自G4Material），那将意味着“逻辑体是一种材料”，这在逻辑上是错误的，并且会导致一个极其僵化和不切实际的设计。通过选择组合，Geant4的架构师们创造了一个高度模块化的系统，用户可以自由地将任何G4VSolid定义的形状与任何G4Material定义的材料组合起来，从而构建出千变万化的探测器世界。这是Geant4工具包强大能力的根基。

### **1.5 多态与抽象：接口的力量**

抽象是指定义一个通用的“接口”或“契约”，而不涉及具体的实现细节。这通常通过包含“纯虚函数”的抽象基类来完成。多态（字面意思为“多种形态”）则是指程序能够通过这个通用接口与不同派生类的对象进行交互，并在运行时自动选择调用哪个对象的具体实现。

对于任何Geant4用户来说，这是最关键、最需要理解的OOP概念。Geant4的核心（Kernel）被设计成与任何具体的实验完全无关 [15](#ref-15)，它正是通过抽象机制来实现这一点的。

* Geant4框架要求用户必须编写几个自己的类，这些类需要继承自Geant4提供的一系列抽象基类，其中最重要的三个是G4VUserDetectorConstruction（探测器构建）、G4VUserPhysicsList（物理列表）和G4VUserPrimaryGeneratorAction（初始粒子行为） [8](#ref-8)。  
* 以G4VUserDetectorConstruction为例，它内部包含一个纯虚函数：virtual G4VPhysicalVolume* Construct() = 0; [17](#ref-17)。这里的= 0语法明确告诉编译器：这个基类只定义了一个“契约”——任何想要定义探测器几何的类，都**必须**提供一个名为Construct、返回G4VPhysicalVolume*类型的方法——但基类自身不提供任何实现。  
* Geant4的主控类G4RunManager会持有一个指向G4VUserDetectorConstruction对象的指针 [16](#ref-16)。它不知道也不关心用户具体定义的类叫什么名字（是MyDetector还是Experiment7Detector）。它只知道，这个指针指向的对象遵守了G4VUserDetectorConstruction的契约，因此它一定有一个可以被调用的Construct()方法。在模拟初始化阶段，G4RunManager就会通过这个基类指针调用Construct()方法，从而执行用户编写的具体几何构建代码 [16](#ref-16)。

这种基于抽象基类的用户接口设计，是使Geant4成为一个真正“工具包”的核心设计模式。它在Geant4内核和用户代码之间划定了一条清晰的界线，并提供了一系列“插件点”。用户可以将自己的定制代码（探测器、物理过程、粒子源）插入到这些插件点中，而完全不需要修改Geant4的源代码。这实现了最高程度的“解耦”，也是面向对象框架设计的精髓所在。Geant4内核定义了**何时**做某事（例如，“在初始化时，我要构建几何”），抽象基类定义了**做什么**（“构建几何意味着调用一个名为Construct的方法”），而用户的具体派生类则定义了**如何做**（“我的Construct方法要创建一个水箱和一个铅筒”）。这种责任的明确划分，造就了Geant4的强大与灵活。

## **第二部分：粒子的生命周期——Geant4模拟中的数据流与对象交互**

理解了OOP的基本原则后，我们现在可以追踪一个粒子从诞生到湮灭的全过程，深入探究在这一过程中，数据是如何在不同的类之间流动和传递的。

### **2.1 总指挥：G4RunManager与模拟初始化**

G4RunManager是整个模拟过程的总指挥和最高控制器 [16](#ref-16)。它通常以“单例”（Singleton）模式存在，即在整个程序运行期间只有一个实例，并作为用户main()函数与Geant4内核交互的主要API。

模拟开始时的信息流如下：

1. 在用户的main()函数中，首先创建G4RunManager的一个实例（对于多线程应用，则创建其派生类G4MTRunManager的实例） [16](#ref-16)。  
2. 接着，用户创建他们自己编写的、继承自Geant4抽象基类的那些强制性类的实例，例如MyDetectorConstruction, MyPhysicsList, MyActionInitialization。  
3. 用户通过调用G4RunManager提供的方法，将这些自己创建的对象“注册”给总指挥。例如，runManager->SetUserInitialization(new MyDetectorConstruction()); [11](#ref-11)。  
4. 这里最关键的一步是，SetUserInitialization方法接受的参数类型是指向基类的指针，即G4VUserDetectorConstruction*。G4RunManager并不知道MyDetectorConstruction这个具体类型，它只通过抽象基类的接口来与这个对象沟通。这正是多态的实际应用。  
5. 当用户调用runManager->Initialize()时，G4RunManager内部会找到它之前保存的那个探测器构建指针，并调用其Construct()方法 [17](#ref-17)。这个调用会触发用户代码的执行，从而完成整个探测器几何的构建。

G4RunManager的角色就像一个“管理者的管理者”，它通过将具体的任务（如构建几何、设置物理过程）委托给用户提供的专业对象来协调整个模拟。这种模式被称为“控制反转”（Inversion of Control），即由框架（Geant4内核）来调用用户的代码，而不是反过来。这清晰地回答了“一个类如何知道另一个类的信息”：用户通过注册（一种依赖注入的形式），主动将自己的对象信息（以指针的形式）告知G4RunManager。G4RunManager则通过预先定义好的抽象接口（基类中的虚函数）来影响和调用用户的对象。

### **2.2 粒子源：G4VUserPrimaryGeneratorAction与G4ParticleGun**

这个阶段负责定义每个模拟“事件”（Event）的初始状态，也就是产生最初的“粒子束” [20](#ref-20)。

粒子产生过程中的信息流如下：

1. 在每个事件开始时，G4RunManager会调用用户PrimaryGeneratorAction对象中的GeneratePrimaries(G4Event* anEvent)方法（这个对象也是在初始化时注册的），并传入一个指向当前G4Event对象的指针 [22](#ref-22)。G4Event对象是用来存储该事件所有信息的容器。  
2. 在用户自己的GeneratePrimaries方法内部，通常会与一个具体的粒子生成器对象进行交互，最常见的就是G4ParticleGun（粒子枪） [23](#ref-23)。  
3. 用户的代码通过调用G4ParticleGun实例的公共“setter”方法来配置要发射的粒子的属性，例如：fparticleGun->SetParticleEnergy(100.*MeV);、fparticleGun->SetParticlePosition(...)等 [22](#ref-22)。这是一种典型的“使用”（Uses-A）关系：PrimaryGeneratorAction类**使用**了一个G4ParticleGun对象来完成它的工作。  
4. 配置完成后，用户的代码调用fparticleGun->GeneratePrimaryVertex(anEvent); [22](#ref-22)。  
5. 在G4ParticleGun::GeneratePrimaryVertex方法的内部，G4ParticleGun对象会利用它自己内部存储的配置数据（能量、位置等），创建新的对象：一个G4PrimaryVertex（初始作用点）和一个或多个G4PrimaryParticle（初始粒子）。  
6. 最后，它通过调用anEvent->AddPrimaryVertex(vertex);，将新创建的G4PrimaryVertex对象添加到从G4RunManager一路传递过来的G4Event对象中 [24](#ref-24)。

这个过程清晰地展示了数据是如何通过一系列方法调用和对象参数传递的。G4RunManager创建了一个空的G4Event容器并将其传递给用户的PrimaryGeneratorAction。PrimaryGeneratorAction利用G4ParticleGun创建了包含初始粒子信息的G4PrimaryVertex。G4ParticleGun再将这个信息填充到G4Event容器中。至此，初始粒子的状态数据已经成功地从用户的控制范围转移到了Geant4内核的事件管理系统中，为接下来的追踪过程做好了准备。

### **2.3 关键时刻：追踪、步进与相互作用**

这是模拟的核心环节，粒子在几何体中穿行，并与物质发生相互作用。这里的数据流动快速而精细。

此阶段的关键对象包括：

* G4Track：代表一个正在运动中的粒子。它包含了粒子的所有动态信息，如动能、动量、当前位置和全局时间 [20](#ref-20)。  
* G4Step：一个临时性的对象，代表粒子在两次相互作用之间走过的一小“步”。它是记录单次相互作用所有信息的中心数据枢纽 [21](#ref-21)。

单步追踪中的信息流如下：

1. G4TrackingManager（追踪管理器）从待处理的粒子栈中取出一个G4Track。  
2. 它向物理过程和几何导航器“征求意见”，以确定这一步的最长可能步长。  
3. 一个G4Step对象被创建，并开始被填充信息。  
4. **信息汇集**：G4Step的PreStepPoint（步前点）从G4Track对象获取了粒子的动能、动量等信息，并记录了当前所在的物理体。为了知道粒子所在的材料是什么，PreStepPoint通过其G4TouchableHandle访问到当前的G4VPhysicalVolume，再通过它找到对应的G4LogicalVolume，最后调用逻辑体的GetMaterial()方法获得材料信息 [25](#ref-25)。通过这种方式，G4Step就“知道”了粒子正处于何种材料之中。  
5. **物理过程介入**：确定了这一步的终点和原因（例如，由康普顿散射过程所限制）后，相应的物理过程对象被调用。这个过程对象可以访问G4Step，读取其中的粒子能量和材料属性。  
6. **记录结果**：物理过程计算出相互作用的结果（能量损失、方向改变、次级粒子的产生等），并更新粒子的状态。这个新的状态被记录在G4Step的PostStepPoint（步后点）中。同时，G4Step对象自身也会被更新，记录下这一步的总能量沉积等摘要信息 [25](#ref-25)。

#### **通过G4UserSteppingAction访问数据**

这正是用户查询的核心所在：当相互作用发生时，用户如何获取这些信息？

1. 在G4Step对象被完全填充（包含了步前、步后以及能量沉积等所有信息）之后，G4TrackingManager会调用用户自定义的UserSteppingAction(const G4Step* aStep)方法 [27](#ref-27)。  
2. 内核将一个指向刚刚完成的G4Step对象的const指针传递给这个方法。const关键字非常重要，它意味着用户代码只能读取G4Step中的信息，而不能修改它，从而保证了追踪过程的完整性和一致性。  
3. 用户的SteppingAction类通过这个被赋予的指针，调用其公共getter方法，就能“知道”这一步中发生的所有事情：  
   * 通过aStep->GetTotalEnergyDeposit()获取能量沉积 [25](#ref-25)。  
   * 通过aStep->GetPreStepPoint()->GetMaterial()->GetName()获取粒子所在材料的名称 [25](#ref-25)。  
   * 通过aStep->GetPostStepPoint()->GetProcessDefinedStep()->GetProcessName()获取是哪个物理过程限制了这一步 [25](#ref-25)。  
4. 用户在自己的代码中获取这些数据后，可以将其传递给其他自定义的分析对象，例如，将能量沉积值累加到在RunAction或EventAction类中定义的总能量变量上 [28](#ref-28)。

G4Step对象的设计是“数据传输对象”（Data Transfer Object, DTO）模式的一个典范。它是一个临时存在的“信使”，其唯一职责就是从多个源头（G4Track、G4LogicalVolume、物理过程等）收集数据，打包成一个方便的整体，然后传递给任何对此感兴趣的角色（比如用户的UserSteppingAction）。它是连接Geant4内核微观行为与用户宏观数据收集的桥梁。

## **第三部分：类关系的综合解析**

### **3.1 类之间如何“互相了解”：机制总结**

通过以上对粒子生命周期的追踪，我们可以总结出Geant4中类与类之间实现信息交换和相互影响的几种核心机制：

* **直接拥有（组合 / "Has-A"）**：一个类将另一个类的对象（或指针）作为自己的成员变量。这通常用于表示长期、稳定的“整体-部分”关系。例如，G4LogicalVolume在其定义中就包含了G4VSolid*和G4Material*成员，因此它从创建之初就“知道”自己的形状和材料 [12](#ref-12)。  
* **继承（"Is-A"）**：子类自动地“知道”其父类的公共接口。这使得代码可以通过父类接口与子类对象交互，而无需知道子类的具体类型。例如，任何需要G4VSolid的代码都可以直接操作G4Box对象 [10](#ref-10)。  
* **方法参数传递（"Uses-A" / "Depends-on-A"）**：一个对象通过其方法的参数，被临时地赋予对另一个对象的访问权（通常是指针或引用）。这是传递瞬时信息或事件相关数据的最常用方式。例如，UserSteppingAction在其UserSteppingAction方法中被给予一个const G4Step*，它仅在该方法执行期间“知道”这个特定G4Step的信息 [27](#ref-27)。  
* **全局访问（单例）**：某些管理器类被设计为全局唯一的，程序的任何部分都可以通过一个静态方法获取到它的实例。例如，任何代码都可以通过调用G4NistManager::Instance()来获取NIST材料数据库管理器的指针，从而查询预定义的材料 [8](#ref-8)。这适用于提供全局性、状态化服务的对象。

### **3.2 Geant4中的类关系一览表**

为了将上述抽象概念与Geant4的具体实践相结合，下表总结了这些关系及其在Geant4中的典型应用。这张表可以作为快速参考，帮助理解不同类之间是如何相互依赖和影响的。

| 关系类型 | 概念含义 | Geant4 示例 | 信息共享方式 |
| :---- | :---- | :---- | :---- |
| **继承** | “是一个” | G4Box **是一个** G4VSolid 10 | 子类 (G4Box) 自动继承父类 (G4VSolid) 的公共/受保护接口和成员。 |
| **组合** | “有一个” | G4LogicalVolume **有一个** G4Material 和一个 G4VSolid 9 | 拥有者类 (G4LogicalVolume) 将被拥有对象的指针 (G4Material\*) 作为其成员变量持有。 |
| **关联/使用** | “使用一个” | MyPrimaryGeneratorAction **使用一个** G4ParticleGun 22 | 一个对象持有另一个对象的实例，并调用其公共方法来完成任务。关系通常不如组合那样稳定。 |
| **依赖** | “依赖于一个” | UserSteppingAction **依赖于一个** G4Step 27 | 一个对象在其方法的参数中接收另一个对象的临时指针/引用。它使用该对象，但不拥有它。 |
| **多态** | “表现得像一个” | G4RunManager 将 MyDetectorConstruction **看作一个** G4VUserDetectorConstruction 16 | 通过基类指针/引用进行通信，允许 G4RunManager 在不知道具体派生类的情况下调用接口方法 (Construct())。 |

### **3.3 结论：面向对象的优势**

Geant4的面向对象架构是其取得巨大成功的核心。通过本文的分析，我们可以看到这种设计如何直接促成了Geant4的关键特性：

* **可扩展性**：用户可以方便地添加新的物理过程、几何实体或粒子源，而无需修改Geant4内核。他们只需继承自相应的抽象基类，并实现其定义的接口即可 [6](#ref-6)。  
* **可维护性**：封装原则将内部实现与外部接口分离，使得Geant4开发团队可以在不破坏用户现有代码的前提下，持续优化和改进内核算法。  
* **清晰性**：代码的结构清晰地反映了真实物理实验的逻辑结构。例如，实体（继承）、逻辑体（组合）和物理体之间的关系，直观地映射了从抽象形状到具体空间定位的构建过程，使代码更易于理解和推理。  
* **灵活性**：正是由于核心组件与具体应用的高度解耦，Geant4才能成为一个通用工具包，被广泛应用于高能物理、空间科学、医学物理（如放射治疗和成像）、辐射防护等截然不同的领域 [3](#ref-3)。

综上所述，面向对象编程不仅仅是一种编程风格，更是一种强大的思想体系。它通过将复杂问题分解为一系列可控、可交互的独立对象，成功地为Geant4提供了管理复杂性、适应未来需求的坚实基础。对于用户而言，理解这些核心原则和设计模式，是掌握Geant4并充分发挥其强大功能的关键。

#### **引用的著作**

<a id="ref-1"></a>1. en.wikipedia.org， [https://en.wikipedia.org/wiki/Geant4\#:\~:text=Geant4%20(for%20GEometry%20ANd%20Tracking,programming%20(in%20C%2B%2B).](https://en.wikipedia.org/wiki/Geant4#:~:text=Geant4%20\(for%20GEometry%20ANd%20Tracking,programming%20\(in%20C%2B%2B\).)  
<a id="ref-2"></a>2. Geant4 - Wikipedia， [https://en.wikipedia.org/wiki/Geant4](https://en.wikipedia.org/wiki/Geant4)  
<a id="ref-3"></a>3. Geant4 - CERN Knowledge Transfer， [https://knowledgetransfer.web.cern.ch/technologies/geant4](https://knowledgetransfer.web.cern.ch/technologies/geant4)  
<a id="ref-4"></a>4. Help: Geant4 tools - SPENVIS， [https://www.spenvis.oma.be/help/background/geant4/geant4.html](https://www.spenvis.oma.be/help/background/geant4/geant4.html)  
<a id="ref-5"></a>5. Introduction to Geant4 - IN2P3 Events Directory (Indico)， [https://indico.in2p3.fr/event/29153/contributions/120344/attachments/76104/110331/IntroductionToGeant4.pdf](https://indico.in2p3.fr/event/29153/contributions/120344/attachments/76104/110331/IntroductionToGeant4.pdf)  
<a id="ref-6"></a>6. Geant4 Architecture Overview: Design, Capabilities, Dependencies, and Processes PowerPoint Presentation - ID:9631973 - SlideServe， [https://www.slideserve.com/myrad/geant-4-s-architecture-powerpoint-ppt-presentation](https://www.slideserve.com/myrad/geant-4-s-architecture-powerpoint-ppt-presentation)  
<a id="ref-7"></a>7. Geant4: G4Box Class Reference， [https://apc.u-paris.fr/~franco/g4doxy/html/classG4Box.html](https://apc.u-paris.fr/~franco/g4doxy/html/classG4Box.html)  
<a id="ref-8"></a>8. Geant4 - Detector construction - Agenda INFN， [https://agenda.infn.it/event/10583/sessions/490/attachments/2925/3214/materials-and_geometry.pdf](https://agenda.infn.it/event/10583/sessions/490/attachments/2925/3214/materials-and_geometry.pdf)  
<a id="ref-9"></a>9. Geant4: A Simulation toolkit， [https://ecolephysique.sciencesconf.org/data/program/G4_LIO_w3_geometries.pdf](https://ecolephysique.sciencesconf.org/data/program/G4_LIO_w3_geometries.pdf)  
<a id="ref-10"></a>10. Geant4.10: G4Box Class Reference， [https://apc.u-paris.fr/~franco/g4doxy4.10/html/class_g4_box.html](https://apc.u-paris.fr/~franco/g4doxy4.10/html/class_g4_box.html)  
<a id="ref-11"></a>11. Geant4 Geometry - Indico， [https://indico.bnl.gov/event/12272/contributions/51346/attachments/35564/58062/Geant4_Geometry.pdf](https://indico.bnl.gov/event/12272/contributions/51346/attachments/35564/58062/Geant4_Geometry.pdf)  
<a id="ref-12"></a>12. Geant4-11: G4LogicalVolume Class Reference， [https://apc.u-paris.fr/~franco/g4doxy4.11/html/classG4LogicalVolume.html](https://apc.u-paris.fr/~franco/g4doxy4.11/html/classG4LogicalVolume.html)  
<a id="ref-13"></a>13. Detector Description: Basics - geant4.web.cern.ch， [https://geant4-internal.web.cern.ch/sites/default/files/geant4/collaboration/working_groups/geometry/training/D2-Basics.pdf](https://geant4-internal.web.cern.ch/sites/default/files/geant4/collaboration/working_groups/geometry/training/D2-Basics.pdf)  
<a id="ref-14"></a>14. Geant4 Geometry - Geant4 @ IN2P3， [https://geant4.in2p3.fr/IMG/pdf_Lecture-Geometry.pdf](https://geant4.in2p3.fr/IMG/pdf_Lecture-Geometry.pdf)  
<a id="ref-15"></a>15. Preliminaries — Geant4 Beginner Course documentation - Read the Docs， [https://geant4-beginner-course.readthedocs.io/en/latest/course-doc/Preliminaries.html](https://geant4-beginner-course.readthedocs.io/en/latest/course-doc/Preliminaries.html)  
<a id="ref-16"></a>16. Run — Book For Toolkit Developers 11.3 documentation - Geant4， [https://geant4.web.cern.ch/documentation/dev/bftd_html/ForToolkitDeveloper/OOAnalysisDesign/Run/run.html](https://geant4.web.cern.ch/documentation/dev/bftd_html/ForToolkitDeveloper/OOAnalysisDesign/Run/run.html)  
<a id="ref-17"></a>17. Geant4: G4VUserDetectorConstruction Class Reference， [https://apc.u-paris.fr/~franco/g4doxy/html/classG4VUserDetectorConstruction.html](https://apc.u-paris.fr/~franco/g4doxy/html/classG4VUserDetectorConstruction.html)  
<a id="ref-18"></a>18. Geant4: G4RunManager Class Reference， [https://apc.u-paris.fr/~franco/g4doxy/html/classG4RunManager.html](https://apc.u-paris.fr/~franco/g4doxy/html/classG4RunManager.html)  
<a id="ref-19"></a>19. Geant4 User's Guide for Toolkit Developers， [https://geant4.web.cern.ch/documentation/dev/bftd_pdf/BookForToolkitDevelopers.pdf](https://geant4.web.cern.ch/documentation/dev/bftd_pdf/BookForToolkitDevelopers.pdf)  
<a id="ref-20"></a>20. Geant4 Kernel - Indico， [https://indico.bnl.gov/event/12272/contributions/51345/attachments/35563/58061/Geant4_Kernel1.pdf](https://indico.bnl.gov/event/12272/contributions/51345/attachments/35563/58061/Geant4_Kernel1.pdf)  
<a id="ref-21"></a>21. Interaction with the Geant4 kernel – part 1 - Indico Global， [https://indico.global/event/11040/contributions/103121/attachments/47529/90021/Pandola%20-%20Kernel%20Lecture%20-%201.pdf](https://indico.global/event/11040/contributions/103121/attachments/47529/90021/Pandola%20-%20Kernel%20Lecture%20-%201.pdf)  
<a id="ref-22"></a>22. III. Primary Particles, User Actions， [https://geant4-ed-project.pages.in2p3.fr/geant4-ed-web/docs/primary_particles.pdf](https://geant4-ed-project.pages.in2p3.fr/geant4-ed-web/docs/primary_particles.pdf)  
<a id="ref-23"></a>23. Primary Particle - CERN Indico， [https://indico.cern.ch/event/776050/contributions/3240644/attachments/1788889/2913530/PrimaryParticle.pdf](https://indico.cern.ch/event/776050/contributions/3240644/attachments/1788889/2913530/PrimaryParticle.pdf)  
<a id="ref-24"></a>24. Geant4: G4ParticleGun Class Reference， [https://apc.u-paris.fr/~franco/g4doxy/html/classG4ParticleGun.html](https://apc.u-paris.fr/~franco/g4doxy/html/classG4ParticleGun.html)  
<a id="ref-25"></a>25. Tracks and steps — FrequentlyAskedQuestions 11.3 documentation， [https://geant4.web.cern.ch/documentation/dev/faq_html/FAQ/tracksAndSteps.html](https://geant4.web.cern.ch/documentation/dev/faq_html/FAQ/tracksAndSteps.html)  
<a id="ref-26"></a>26. G4Step Class Reference - Geant4， [https://hurel.hanyang.ac.kr/Geant4/Doxygen/9.6.p02/html/class_g4_step.html](https://hurel.hanyang.ac.kr/Geant4/Doxygen/9.6.p02/html/class_g4_step.html)  
<a id="ref-27"></a>27. Geant4:User Actions and Analysis - CERN Indico， [https://indico.cern.ch/event/422168/contributions/1903302/subcontributions/170176/attachments/888132/1249407/userActions.pdf](https://indico.cern.ch/event/422168/contributions/1903302/subcontributions/170176/attachments/888132/1249407/userActions.pdf)  
<a id="ref-28"></a>28. SLAC Geant4 Tutorial Hands-On 4， [https://www.slac.stanford.edu/xorg/geant4/SLACTutorial14/HandsOn4/](https://www.slac.stanford.edu/xorg/geant4/SLACTutorial14/HandsOn4/)