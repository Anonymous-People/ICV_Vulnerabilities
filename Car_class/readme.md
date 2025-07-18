# Pending Organization

The main text of this section has not yet been organized. You can first refer to the following LaTeX source code:

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

\subsection{Nationality-Based Mapping}

\subsubsection{Relation between Nations and Locations}
To reveal the differences in ICV security across countries of manufacture, we analyzed the distribution of vulnerabilities across different modules in ICVs from various nations.
ICVs manufactured in China account for the vast majority of all recorded vulnerabilities (88.6\%).
This is largely due to the lack of unified and mature standards for ICV production, with many regulations still in trial stages, leading to heterogeneous network architectures and protection mechanisms across manufacturers.
In contrast, vulnerabilities in American vehicles are predominantly concentrated in in-vehicle components (such as ECUs and IVIs), accounting for as much as 89.3\%, with almost no cloud platform vulnerabilities.
German ICVs exhibit a more balanced distribution, with 59.4\% of vulnerabilities involving cloud platforms and APPs, and 40.6\% tied to in-vehicle systems—indicating simultaneous emphasis on internal and external system protection.

\subsubsection{Relation between Nations and Types}
From a vulnerability type perspective (Table~\ref{tab: typeplus}), authorization issues dominate across all nations but are especially prominent in Chinese ICVs (36.87\%), suggesting persistent challenges in access control and identity verification.
Chinese vehicles also show high instances of information leakage (104) and injection vulnerabilities (73), indicating gaps in secure data handling and input sanitization. German vehicles present a more distributed type profile, though authorization flaws remain primary.
In contrast, American vehicles, despite having fewer total vulnerabilities, show a low proportion of information leakage (7.1\%), highlighting concerns with data exposure and insufficient boundary protections.
These patterns reflect differing priorities and levels of cybersecurity maturity among ICV-producing nations.


\subsection{APP class}

The app in the competition is the default app provided by the car manufacturer, developed often in Java, and serves informational and entertainment functions, such as a car owner forum and remote door unlocking.
Therefore, we are unable to categorize the app. 
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

