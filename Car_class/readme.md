```
\documentclass[sigconf, twoside, twocolumn]{acmart}
\usepackage{multirow}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{caption}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{enumitem}
\usepackage{mdframed}
\usepackage{xcolor}
\usepackage{lipsum}
\usepackage{tcolorbox} 
\usepackage{pifont}
\usepackage{diagbox}
\usepackage[flushleft]{threeparttable}
\usepackage{tikz}
\usepackage{ulem}
\usepackage{flushend}
\usepackage{tabularx}
\usepackage{appendix}
\usepackage{subfigure}
\usepackage{makecell}

\begin{document}

\section{ICV Class Taxonomy}\label{vehicletaxonomy}

As described in Section 3.1.3, the participating ICVs were categorized along four dimensions: country/region, EPA size, SAE automation level, and power type.
This section analyzes the correlation between these categories and both vulnerability locations and types, aiming to reveal distribution patterns and identify common security weaknesses across different classes of vehicles.
Note that this section focuses on the mappings related to EPA size, SAE level, and power type; the analysis of vulnerabilities by country/region is provided in our publicly available dataset.



\subsection{EPA size mapping}

\subsubsection{Relation between EPA sizes and vulnerability locations}
As demonstrated in Table~\ref{tab: locationplus}, the distribution of vulnerabilities across system modules varies notably with EPA size classifications.
IVI-related vulnerabilities are prevalent across all categories but are especially concentrated in SUVs, which exhibit an average of 5.6 IVI vulnerabilities per vehicle—significantly higher than sedans (3.4) and MPVs (2.0).
This suggests that SUVs may incorporate more complex or feature-rich IVI systems, increasing the attack surface.
Similarly, cloud platform vulnerabilities are most prominent in SUVs (3.2), reflecting greater integration with cloud-based services.
Notably, 140 cloud platform vulnerabilities are cross-category, affecting multiple vehicle types (two or even all three, such as SUVs, sedans, and MPVs) from the same manufacturer.
This indicates a shared backend infrastructure or common components across different ICVs, amplifying the impact of a single vulnerability.

\subsubsection{Relation between EPA sizes and vulnerability types}
As shown in Table~\ref{tab: locationplus}, vehicles across different EPA size classifications exhibit significant differences in vulnerability types.
SUVs and sedans have higher average numbers of vulnerabilities per vehicle (12.7 and 8.8, respectively), while MPVs show the lowest average (3.0).
This may be attributed to the simpler software architectures and fewer integrated digital services in MPVs, particularly in business-oriented models.
Authorization vulnerabilities are the most common across all categories, with SUVs reporting the highest number (4.9 per vehicle).
SUVs also lead in OS and injection vulnerabilities, which may be linked to their more complex or advanced infotainment systems and connectivity features.
Sedans exhibit similar trends, though with slightly lower counts across most vulnerability types.



\subsection{SAE level mapping}
\subsubsection{Relation between SAE levels and vulnerability locations}
Table~\ref{tab: locationplus} shows that SAE L2 vehicles have the highest average number of vulnerabilities, with 11.6 per vehicle.
Among all automation levels, the IVI system is the most vulnerable component, particularly in L2 vehicles, where IVI vulnerabilities average 5.1 per vehicle.
Compared to L3, L2 systems still heavily rely on human-machine interfaces such as voice control and multimedia, making IVI functions more complex and interface-rich, thereby expanding the attack surface. This indicates that mid-level autonomous systems like L2, which are undergoing rapid functional integration, tend to lag behind in security protection, making them a critical focus for current vulnerability mitigation efforts.



\subsubsection{Relation between SAE levels and vulnerability types}
Authorization vulnerabilities are the most common across all automation levels, with L2 vehicles averaging 4.5 per vehicle—more than three times the count in L1 (1.3).
This indicates that L2 systems, which often require coordination between multiple modules and user permission management, are more susceptible to access control flaws.
L2 vehicles also lead in injection, OS, and DoS vulnerabilities, further underscoring the security burden associated with intermediate levels of automation.
Overall, due to their high complexity and lack of mature protection mechanisms, L2 systems have emerged as a critical bottleneck in ICV security.

\subsection{Power type mapping}
\subsubsection{Relation between power types and vulnerability locations}
Electric vehicles exhibit the highest average number of vulnerabilities, followed by hybrid and petrol vehicles, indicating that increased electrification and connectivity significantly expand the system's attack surface.
Among all power types, IVI is the most common vulnerability location, with hybrid vehicles showing the highest number of IVI-related vulnerabilities—likely due to the integration of dual power systems and more human-machine interaction features, resulting in greater system complexity.
The APP module shows a higher frequency of vulnerabilities in electric vehicles, reflecting their stronger reliance on mobile applications and connectivity functions.
Although petrol vehicles have fewer overall vulnerabilities, security risks still exist in the T-Box and ECU modules, suggesting that traditional vehicles are also exposed to new attack surfaces as they evolve toward increased intelligence.


\subsubsection{Relation between power types and vulnerability types}
In electric vehicles, authorization vulnerabilities (4.3) and OS vulnerabilities (2.0) are the most prominent, indicating significant security risks in access control and system management.
This may be attributed to the widespread use of custom operating systems and multi-module coordination.
Hybrid vehicles show a higher concentration of DoS vulnerabilities (1.6), possibly due to the added complexity of integrating intelligent features on top of traditional systems, making resource scheduling more sensitive.
Although petrol vehicles have a lower overall vulnerability count, they still exhibit notable risks in OS and injection vulnerabilities, suggesting that even conventional power platforms face software security challenges during the shift toward intelligent systems.

\begin{table}[t]
\centering
\footnotesize
\setlength{\tabcolsep}{1.0pt}
\caption{Mapping Results of the ICV Class Taxonomy.}
\begin{tabular}{c|c|ccc|ccc|ccc}
\toprule
\multicolumn{2}{c|}{\multirow{2}{*}{\diagbox[width=13em,dir=SE]{Location \& Type}{CarClass}}} & \multicolumn{3}{c|}{EPA size} & \multicolumn{3}{c|}{SAE level} & \multicolumn{3}{c}{Power type}  \\
\cmidrule{3-11}
\multicolumn{2}{l|}{} & SUV & Sedan & MPV & L1& L2& L3& Electric &Hybird&Petrol\\
% \cmidrule{3-15}
\midrule
\multicolumn{2}{c|}{Car count}  & 20 & 24 & 4 &6&36 &  6&22&16&10\\
\midrule
\multirow{8}{*}{Location}& Cloud platform  & 3.2 & 1.6& 1.0 & 1.0 & 2.6 & 0.7&2.0&2.3&2.4  \\			
&IVI & 5.6 & 3.4& 2.0&1.7& 5.1 & 1.3&3.4&5.8&3.4 \\
&APP&0.9 &1.7 & - &- & 1.3& 2.0&2.2&0.1&0.8 \\
&ECU&1.2 & 0.5 & - & 1.3 & 0.7&0.7&1.0&0.4&0.8 \\
&Network & 0.8 & 0.6 & - & 0.3& 0.7 & 0.7&1.0&0.4&0.3  \\
&T-Box& 0.9 & 0.3& - &- & 0.7& -&0.4&0.4&1.0 \\
&Radio& 0.3& 0.5 & - & - &0.5 & -&0.5&0.3&0.2  \\
&Charging pile &-& -&-&-&-&-&-&-&-\\ \midrule
\multirow{9}{*}{Type}&Authorization& 4.9 & 3.1 & 1.0& 1.3& 4.5 & 1.3&4.3&3.6&2.4 \\
&Information leakage & 1.9 & 1.5 & 0.8 & 1.5& 1.6& 1.5&1.1&0.6&0.9 \\
&Injection & 1.1& 0.8& 0.3 & 0.3& 1.1& 0.3&0.1&0.7&0.8\\
&OS& 2.0 & 0.5& 0.3& 0.3& 1.4& 0.3 &2.0&0.6&2.1\\
&DoS & 0.9 & 1.1 & - & 0.3& 1.0& 1.0 &0.6&1.6&0.4\\
&Interception& 0.8 & 0.1 & 0.8& 0.2& 0.9& 0.5&1.0&0.6&0.6\\
&File operation& 0.6& 1.0 & -& 0.3& 0.5& 0.2&0.4&-&0.5\\
&Web-specific& 0.4& 0.2 & -&-& 0.3& 0.2&0.9&1.6&0.9\\
&Memory& 0.2&0.4& - &-& 0.4&-&0.1&0.4&0.3\\
\midrule
\multicolumn{2}{c|}{Average vulnerabilities per car}&12.7& 8.8& 3.0&4.3& 11.6 & 5.3 &10.5&9.6&8.9 \\

\bottomrule
\end{tabular}
\label{tab: locationplus}

\begin{tablenotes}
\item Note: To mitigate the impact of class imbalance among ICV categories, all values in the tables represent the average number of vulnerabilities per vehicle within each category for a given location or vulnerability type.
\end{tablenotes}
\vspace{-4mm}
\end{table}


\subsection{Nationality-Based Mapping}

\subsubsection{Relation between Nations and Locations}
To reveal the differences in ICV security across countries of manufacture, we analyzed the distribution of vulnerabilities across different modules in ICVs from various nations.
As shown in Table~\ref{tab: locationplus}, ICVs manufactured in China account for the vast majority of all recorded vulnerabilities (88.6\%).
This is largely due to the lack of unified and mature standards for ICV production, with many regulations still in trial stages, leading to heterogeneous network architectures and protection mechanisms across manufacturers.
In contrast, vulnerabilities in American vehicles are predominantly concentrated in in-vehicle components (such as ECUs and IVIs), accounting for as much as 89.3\%, with almost no cloud platform vulnerabilities.
German ICVs exhibit a more balanced distribution, with 59.4\% of vulnerabilities involving cloud platforms and APPs, and 40.6\% tied to in-vehicle systems—indicating simultaneous emphasis on internal and external system protection.

\subsubsection{Relation between Nations and Types}
From a vulnerability type perspective (Table~\ref{tab: typeplus}), authorization issues dominate across all nations but are especially prominent in Chinese ICVs (36.87\%), suggesting persistent challenges in access control and identity verification.
Chinese vehicles also show high instances of information leakage (104) and injection vulnerabilities (73), indicating gaps in secure data handling and input sanitization. German vehicles present a more distributed type profile, though authorization flaws remain primary.
In contrast, American vehicles, despite having fewer total vulnerabilities, show a high proportion of information leakage (75\%), highlighting concerns with data exposure and insufficient boundary protections.
These patterns reflect differing priorities and levels of cybersecurity maturity among ICV-producing nations.


, with the highest proportions observed in Small SUVs (37.6\%) and Compact Cars (35.0\%).
This suggests that remote connectivity services are more widely deployed in smaller vehicles, thereby exposing them to greater risks associated with cloud infrastructure.
The IVI system dominates in most size categories, particularly in Standard SUVs and Small SUVs, where it accounts for 42.2\% and 49.5\% of the respective vulnerabilities.
This highlights the high degree of IVI integration in these models, making it a primary attack target.

APP vulnerabilities are mainly concentrated in mid-size and large cars, which tend to incorporate richer mobile application features such as remote control and user interaction.
As vehicle size increases, the proportion of ECU-related vulnerabilities rises significantly, for example, Standard SUVs report 13.0\% of their vulnerabilities in the ECU module, compared to just 4.3\% in Small SUVs. This trend reflects the growing complexity of system architectures in larger vehicles, resulting in a broader attack surface.
Notably, the ``-'' category represents cross-size vulnerabilities, with a large concentration in cloud platforms (140 cases).
This indicates that different ICV types may share a unified cloud service architecture, thereby introducing systemic risks across platforms.

\subsection{APP class}

The app in the competition is the default app provided by the car manufacturer, developed in Java, and serves informational and entertainment functions, such as a car owner forum and remote door unlocking.
herefore, we are unable to categorize the app. 
However, we can classify the 66 app vulnerabilities we have collected into two categories: the first category includes vulnerabilities within the app itself, such as car mileage information leakage and arbitrary account password login; the second category involves vulnerabilities that affect vehicle safety, such as the ability to control the vehicle's unlocking.
As shown in Table ~\ref{APP Table}, it can be observed that while the car manufacturer has implemented some protection for communication between the app and the car, they have overlooked the app's security, leading to vulnerabilities such as owner information leakage and arbitrary account logins.
Therefore, car manufacturers should not only focus on the app's security during communication with the car but also pay attention to the app's full lifecycle security, from the development phase to the usage phase, in order to avoid common basic errors during the development stage, such as information leakage (27),  unauthorized accessing (19), and unvalidated inputs(Command injection (6), SQL injection (1)).


\begin{table}[!t]
\caption{APP}
\begin{tabular}{c|cc|c}
\toprule
Type                   & Self & Car & Sum \\
\midrule
Information leakage    & 25   & 2   & 27  \\
Unauthorized accessing & 19   &     & 19  \\
DoS                    & 7    &     & 7   \\
Command injection      & 5    & 1   & 6   \\
Weak password          & 2    &     & 2   \\
Replay                 & 1    & 1   & 2   \\
SQL injection          & 1    &     & 1   \\
Man-in-the-middle      & 1    &     & 1   \\
Identity spoofing      & 1    &     & 1   \\
\midrule
Sum                    & 62   & 4   & 66  \\
\bottomrule
\end{tabular}
\label{APP Table}
\end{table}

\end{document}
```

