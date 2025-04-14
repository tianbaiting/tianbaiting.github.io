# latex include graphics

use subfloat instead of subfigure.

```
\begin{figure}
    \centering
    \subfloat[The angular coverage of the detectors. \label{polarimeter_angcove}]{
        \includegraphics[width=0.23\textwidth]{tbt_new_img/Pol_angcover.pdf}
    }
    \hfill
    \subfloat[The relationship between the energy and scattering angle. \label{polarimeter_angcover}]{
        \includegraphics[width=0.23\textwidth]{tbt_new_img/Energy_vs_ThetaDc_deg.pdf}
    }
    \caption{detector setting.}
    \label{fig:comparison1}
\end{figure}
```