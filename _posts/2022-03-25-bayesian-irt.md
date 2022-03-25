---
title: "Bayesian Variational Inference for IRT"
date: 2022-03-25
tags:
  - math
categories: blog
toc: false
toc_sticky: false
header:
  teaser: "/../assets/2022-03-17-how-to-fix-sqlfluff/thumbnail.png"
---

Converted star to backslash

Converted vector sings 

In this blog post I want to tell you about **Bayesian Variational Inference for IRT**.

One of our interns is currently working on this project and I'm guiding her  a bit on this.

You can find the paper here: https://arxiv.org/abs/2002.00276

## What is IRT?

Before I can tell you what Bayesian Variational Inference is for IRT, I first need to explain what is IRT.

Item Response Theory (IRT) is a way of modeling human knowledge based on their responses to questions.

In the context of edtech platforms this means that we try to make a model of someone's knowledge based on their answers they give in the platform.

In simple terms the mental model works something like this: We give every student a certain score that we call their **ability**. Then we give every exercise a certain score that we call its **difficulty**. Together, we use the ability and difficulty to calculate the probability that this user (with his ability) can make this exercise (with a difficulty) and call this the **solve probability**.

## The math behind iRT



\begin{equation}
    p(r_{i,j}=1|a_i,d_j) = \frac{1}{1 + e^{-(a_i - d_j)}}
\label{eq:1pl_irt}
\end{equation}
where $r_{i,j}$ is the response by the $i$-th person to the $j$-th item.

There are $N$ people and $M$ items in total.

Each item in the 1PL model is characterized by a single number representing difficulty, $d_j$.

In practice, given a (possibly incomplete) $N \times M$ matrix of observed responses, we want to \textit{infer} the ability of all $N$ people and the characteristics of all $M$ items.

Often, a portion of the $N\times M$ entries are missing.

## Variational inference

The main intuition of variational inference (VI) is to treat inference as an
optimization problem: starting with a family of distributions, the goal is to
pick the one that best approximates the true posterior, by minimizing an
estimate of the mismatch between true and approximate distributions.  We will
first describe VI in the general context of a latent variable model, and then
will apply VI to IRT.

Let $x \in \mathcal{X}$ and $z \in \mathcal{Z}$ represent observed and latent variables, respectively.

In VI we introduce a family of tractable distributions over $z$ (such that we can easily sample and score).

We wish to find the member $q_{\psi^\*(x)} \in \mathcal{Q}$ that minimizes the Kullback-Leibler (KL) divergence between itself and the true posterior:

\begin{equation}
q_{\psi^\*(x)}(z) = \arg \min_{q_{\psi(x)}} KL(q_{\psi(x)}(z) || p(z|x))
\end{equation}

where $\psi(x)$ are parameters that define each distribution.
For example, $\psi(x)$ would be the mean and scale for a Gaussian distribution.
Since the ``best" approximate posterior $q_{\psi^\*(x)}$ depends on the observed variables, its parameters have $x$ as a dependent variable.
To be clear, there is one approximate posterior for every possible value of the observed variables.

Frequently, we need to do inference for many different values of the observed variables $x$. Let $p_{\mathcal{D}}(x)$ be an empirical distribution over the observed variables, which is equivalent to the marginal $p(x)$ if the generative model is correctly specified. Then, the average quality of the variational approximations is measured by

\begin{equation}
    \mathbb{E}_{p_{\mathcal{D}}(x)}\left[ \max_{\psi(x)} \mathbb{E}_{q_{\psi(x)}(z)}\left[\log \frac{p(x,z)}{q_{\psi(x)}(z)}\right] \right]
\end{equation}

In practice, $p_{\mathcal{D}}(x)$ is unknown but we assume access to a dataset $\mathcal{D}$ of examples i.i.d. sampled from $p_{\mathcal{D}}(x)$; this is sufficient to evaluate Eq.~\ref{eq:elbo}.

We have essentially converted inference to an optimization problem of picking the best parameters to maximize an objective function.

We now introduce a few additional details of VI that will be useful in understanding VIBO.

### Amoritzxation

\subsection{Variational Methods}

The main intuition of variational inference (VI) is to treat inference as an
optimization problem: starting with a family of distributions, the goal is to
pick the one that best approximates the true posterior, by minimizing an
estimate of the mismatch between true and approximate distributions.  We will
first describe VI in the general context of a latent variable model, and then
will apply VI to IRT.

Let $x \in \mathcal{X}$ and $z \in \mathcal{Z}$ represent observed and latent variables, respectively.

In VI we introduce a family of tractable distributions over $z$ (such that we can easily sample and score).

We wish to find the member $q_{\psi^\*(x)} \in \mathcal{Q}$ that minimizes the Kullback-Leibler (KL) divergence between itself and the true posterior:

\begin{equation}
q_{\psi^\*(x)}(z) = \arg \min_{q_{\psi(x)}} \KL(q_{\psi(x)}(z) || p(z|x))
\end{equation}

where $\psi(x)$ are parameters that define each distribution.
For example, $\psi(x)$ would be the mean and scale for a Gaussian distribution.
Since the ``best" approximate posterior $q_{\psi^\*(x)}$ depends on the observed variables, its parameters have $x$ as a dependent variable.
To be clear, there is one approximate posterior for every possible value of the observed variables.

Frequently, we need to do inference for many different values of the observed variables $x$. Let $p_{\mathcal{D}}(x)$ be an empirical distribution over the observed variables, which is equivalent to the marginal $p(x)$ if the generative model is correctly specified. Then, the average quality of the variational approximations is measured by

\begin{equation}
    \mathbb{E}_{p_{\mathcal{D}}(x)}\left[ \max_{\psi(x)} \mathbb{E}_{q_{\psi(x)}(z)}\left[\log \frac{p(x,z)}{q_{\psi(x)}(z)}\right] \right]
\end{equation}

In practice, $p_{\mathcal{D}}(x)$ is unknown but we assume access to a dataset $\mathcal{D}$ of examples i.i.d. sampled from $p_{\mathcal{D}}(x)$; this is sufficient to evaluate Eq.~\ref{eq:elbo}.

We have essentially converted inference to an optimization problem of picking the best parameters to maximize an objective function.

We now introduce a few additional details of VI that will be useful in understanding VIBO.


### Model laerning

### Stochastic gradient descent

### Reparametrization

\textbf{Model Learning}$\quad$
So far we have assumed a fixed generative model $p(x, z)$.
However, often we can only specify a family of possible models $p_\theta(x|z)$ parameterized by $\theta$.
The symmetric challenge (to approximate inference) is to choose $\theta$ whose model best explains the evidence.
Naturally, we do so by maximizing the log marginal likelihood of the data

\begin{equation}
    \log p_\theta(x) = \log \int_{z} p_\theta(x,z) dz
\end{equation}

Using Eq., we derive the Evidence Lower Bound (ELBO) with $q_{\phi}(z|x)$ as our inference model

\begin{equation}
    \log p_\theta(x) \geq \mathbb{E}_{q_\phi(z|x)}\left[ \log \frac{p_\theta(x,z)}{q_\phi(z|x)} \right] \triangleq \textup{ELBO}
\end{equation}

We can jointly optimize $\phi$ and $\theta$ to maximize the ELBO.
We have the option to parameterize $p_\theta(x|z)$ and $q_\phi(z|x)$ with deep neural networks, as is common with the VAE \cite{kingma2013auto}, yielding an extremely flexible space of distributions.

\textbf{Stochastic Gradient Estimation}$\quad$
The gradients of the ELBO (Eq.~\ref{eq:elbo:vae}) with respect to $\phi$ and $\theta$ are:
\begin{align}
    \nabla_\theta \textup{ELBO} &= \mathbb{E}_{q_\phi(z|x)}[\nabla_\theta \log p_\theta(x,z)]]\label{eq:grad:theta} \\
    \nabla_\phi \textup{ELBO} &= \nabla_\phi \mathbb{E}_{q_\phi(z|x)}[ \log p_\theta(x,z)] \label{eq:grad:phi}
\end{align}
Eq.~\ref{eq:grad:theta} can be estimated using Monte Carlo samples.
However, as it stands, Eq.~\ref{eq:grad:phi} is difficult to estimate as we cannot distribute the gradient inside the inner expectation.
For certain families $\mathcal{Q}$, we can use a reparameterization trick.

\textbf{Reparameterization Estimators}$\quad$

Reparameterization is the technique of removing sampling from the gradient computation graph \cite{kingma2013auto,rezende2014stochastic}.
In particular, if we can reduce sampling $z \sim q_\phi(z|x)$ to sampling from a parameter-free distribution $\eps \sim p(\eps)$ plus a deterministic function application, $z = g_\phi(\eps)$, then we may rewrite Eq.~\ref{eq:grad:phi} as:

\begin{equation}
\nabla_\phi \textup{ELBO} = \mathbb{E}_{p(\eps)} [ \nabla_{z} \log \frac{p_\theta(x,z(\eps))}{q_\phi(z(\eps)|z)} \nabla_\phi g_\phi(\eps) ]
\end{equation}

which now can be estimated efficiently by Monte Carlo (the gradient is inside the expectation).
A benefit of reparameterization over alternative estimators (e.g. score estimator \cite{mnih2014neural} or REINFORCE \cite{williams1992simple}) is lower variance while remaining unbiased.
A common example is if $q_\phi(z|x)$ is Gaussian $\mathcal{N}(\mu,\sigma^2)$ and we choose $p(\eps)$ to be $\mathcal{N}(0, 1)$, then $g(\eps) = \eps * \sigma + \mu$.

## VIBO

Having reviewed the major principles of VI, we will adapt them to IRT.
We call the resulting algorithm VIBO since it is a \textbf{V}ariational approach for \textbf{I}tem response theory based on a novel lower \textbf{BO}und.

We state and prove VIBO in the following theorem.
\begin{thm}
    Let $\va_i$ be the ability for person $i \in [1, N]$ and $\vd_{j}$ be the characteristics for item $j \in [1, M]$. We use the shorthand notation $\vd_{1:M} = (\vd_1, \ldots, \vd_M)$. Let $r_{i,j}$ be the binary response for item $j$ by person $i$. We write $\vr_{i, 1:M} = (r_{i,1}, \ldots r_{i,M})$.
    If we define the VIBO objective as:
    \begin{equation*}
        \textup{VIBO} \triangleq \mathcal{L}_{\text{recon}} + \mathbb{E}_{q_\phi(\vd_{1:M}|\vr_{i,1:M})}[D_{\text{ability}}] +D_{\text{item}}
    \end{equation*}
    where
    \begin{align*}
        \mathcal{L}_{\text{recon}} &= \mathbb{E}_{q_\phi(\va_i, \vd_{1:M}|\vr_{i,1:M})}\left[ \log p_\theta(\vr_{i,1:M}|\va_i, \vd_{1:M}) \right] \\
        D_{\text{ability}} &= \KL(q_\phi(\va_i|\vd_{1:M},\vr_{i,1:M}) || p(\vu_i)) \\
        D_{\text{item}} &= \KL(q_\phi(\vd_{1:M}|\vr_{i,1:M})||p(\vd_{1:M}))
    \end{align*}
    and assume the joint posterior factors as follows
    \begin{equation*}
        q_\phi(\va_i, \vd_{1:M}|\vr_{i,1:M}) = q_\phi(\va_i|\vd_{1:M},\vr_{i,1:M})q_\phi(\vd_{1:M}|\vr_{i,1:M})
    \end{equation*}
    then $\log p(\vr_{i,1:M}) \geq \textup{VIBO}$. In othe words, VIBO is a lower bound on the log marginal probability of person $i$'s responses.
    \label{thm:virtu}
\end{thm}

Thm.~\ref{thm:virtu} leaves several choices up to us, and we opt for the simplest ones.
For instance, the prior distributions are chosen to be independent standard Normal distributions: $p(\va_i) = \prod_{k=1}^K p(a_{i,k})$ and $p(\vd_{1:M}) = \prod_{j=1}^M p(\vd_{j})$ where $p(a_{i,k})$ and $p(\vd_j)$ are $\mathcal{N}(0,1)$.
Further, we found it sufficient to assume $q_\phi(\vd_{1:M}|\vr_{i,1:M}) = q_\phi(\vd_{1:M})= \prod_{j=1}^M q_\phi(\vd_{j})$ although nothing prevents the general case.
Initially, we assume the generative model, $p_\theta(\vr_{i,1:M}|\va_i,\vd_{1:M})$, to be an IRT model (thus $\theta$ is empty); later we explore generalizations.

The posterior $q_\phi(\va_i|\vd_{1:M},\vr_{i,1:M})$ needs to be robust to missing data as often not every person answers every question.
To achieve this, we explore the following family:
\begin{equation}
    q_\phi(\va_i|\vd_{1:M},\vr_{i,1:M}) = \prod_{j=1}^M q_\phi(\va_i|\vd_j,\vr_{i,j})
\end{equation}
If we assume each component $q_\phi(\va_i|\vd_j,\vr_{i,j})$ is Gaussian, then $q_\phi(\va_i|\vd_{1:M},\vr_{i,1:M})$ is Gaussian as well, being a Product-Of-Experts \cite{hinton1999products,wu2018multimodal}.
If item $j$ is missing, we replace its term in the product with the prior, $p(\va_i)$ representing no added information.
We found this design to outperform averaging over non-missing entries: $\frac{1}{M}\sum_{j=1}^M q_\phi(\va_i|\vd_j,\vr_{i,j})$.


As VIBO is a close cousin of the ELBO, we can estimate its gradients with respect to $\theta$ and $\phi$ similarly:
$$
\begin{align*}
    \nabla_\theta \textup{VIBO} &= \nabla_\theta \mathcal{L}_{\text{recon}} \\
    &= \mathbb{E}_{q_\phi(\va_i, \vd_{1:M}|\vr_{i,1:M})}\left[ \nabla_\theta \log p_\theta(\vr_{i,1:M}|\va_i, \vd_{1:M}) \right] \\
    \nabla_\phi \textup{VIBO} &= \nabla_\phi \mathbb{E}_{q_\phi(\vd_{1:M}|\vr_{i,1:M})}[D_{\text{ability}}] + \nabla_\phi D_{\text{item}} \\
    &= \nabla_\phi \mathbb{E}_{q_\phi(\va_i,\vd_{1:M}|\vr_{i,1:M})}\left[\frac{p(\va_i)p(\vd_{1:M})}{q_\phi(\va_i,\vd_{1:M}|\vr_{i,1:M})}\right]
\end{align*}
$$
As in Eq.~\ref{eq:grad:elbo}, we may wish to move the gradient inside the KL divergences by reparameterization to reduce variance.
To allow easy reparameterization, we define all variational distributions $q_\phi(\cdot|\cdot)$ as Normal distributions with diagonal covariance.
In practice, we find that estimating $\nabla_\theta \text{VIBO}$ and $\nabla_\phi \text{VIBO}$ with a single sample is sufficient.
With this setup, VIBO can be optimized using stochastic gradient descent to learn an amortized inference model that maximizes the marginal probability of observed data.
We summarize the required computation to calculate VIBO in Alg.~\ref{alg:vibo}.
% \ndg{either here or in expts section need to say what optimization algorithm was used, and when we decided to stop optimizing (the latter is affects run time directly...)}

\begin{algorithm}[h!]
\SetAlgoLined
    Assume we are given observed responses for person $i$, $\vr_{i1:M}$\;
    Compute $\mu_{\vd}, \sigma^2_{\vd} = q_\phi(\vd_{1:M})$\;
    Sample $\vd_{1:M} \sim \mathcal{N}(\mu_{\vd}, \sigma^2_{\vd})$\;
    Compute $\mu_{\va}, \sigma^2_{\va} = q_\phi(\va_i|\vd_{1:M},\vr_{i,1:M})$\;
    Sample $\va_i \sim \mathcal{N}(\mu_{\va}, \sigma^2_{\va})$\;
    Compute $\mathcal{L}_{\text{recon}} = \log p_\theta(\vr_{i,1:M}|\va_i,\vd_{1:M})$\;
    Compute $D_{\text{ability}} = \KL(\mathcal{N}(\mu_{\va}, \sigma^2_{\va})||\mathcal{N}(0,1))$\;
    Compute $D_{\text{item}} = \KL(\mathcal{N}(\mu_{\vd}, \sigma^2_{\vd})||\mathcal{N}(0,1))$\;
    Compute $\text{VIBO} = \mathcal{L}_{\text{recon}} + D_{\text{ability}} + D_{\text{item}}$
    \caption{VIBO Forward Pass}
    \label{alg:vibo}
\end{algorithm}
A public implementation of VIBO will be available in PyTorch and Pyro \cite{bingham2019pyro} along with a Python package for more practical uses modeled after the R package, MIRT \cite{chalmers2012mirt}.










<!-- Begin Mailchimp Signup Form -->
<link href="//cdn-images.mailchimp.com/embedcode/horizontal-slim-10_7.css" rel="stylesheet" type="text/css">
<style type="text/css">
  #mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; width:100%;}
  /* Add your own Mailchimp form style overrides in your site stylesheet or in this style block.
     We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
</style>
<div id="mc_embed_signup">
<form action="https://gmail.us3.list-manage.com/subscribe/post?u=92fe86c389878585bc87837e8&amp;id=50543deff9" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll">
  <label for="mce-EMAIL">Liked this article and want to hear more? Join 40+ others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
