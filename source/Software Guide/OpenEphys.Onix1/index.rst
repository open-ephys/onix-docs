.. _openephys_onix1ref:

Bonsai ONIX Package
=================================

``OpenEphys.Onix1`` is a `Bonsai <https://bonsai-rx.org/>`__ package for ONIX
hardware. This package contains `Bonsai Operators
<https://bonsai-rx.org/docs/articles/operators.html>`__ for acquiring and
sending data to ONIX hardware.

:Code: https://github.com/open-ephys/bonsai-onix1
:Compatibility: All ONIX hardware, Neuropixels, UCLA miniscopes & variants
:Documentation: https://open-ephys.github.io/bonsai-onix1-docs/index.html

.. raw:: html

        <a href="https://open-ephys.github.io/bonsai-onix1-docs/index.html"><span class="std std-ref custom-card">
        <div class="card text-center page-card">

            <header>
                <h1>Go to the OpenEphys.Onix1 Docs <i class="fas fa-external-link"></i></h1>
            </header>
            <img src="../../_static/images/bonsai-lettering.svg"
            class="page-card-img-marg hover-zoom" alt="OpenEphys.Onix1 bonsai
            package documentation">

        </div>

What is Bonsai?
------------------------------
`Bonsai <https://bonsai-rx.org/>`__ is a visual programming language (think
LabView) for `reactive programming
<https://en.wikipedia.org/wiki/Reactive_programming>`__ with features such as:

- Real-time compilation of workflows to machine code as they are edited
  (zero-overhead).
- A large array of operators for combining and sychronizing asynchronous data
  streams, which is a major issue in other software.
- Lots of support for all sorts of hardware outside of ONIX.

Bonsai is A good choice for accessing the full power of ONIX hardware and
combining it with third-party data sources (e.g. machine vision cameras,
behavioral hardware, etc.), and for real-time processing and manipulation of
data streams. The documentation linked above contains detailed instructions on
how to use Bonsai with ONIX hardware along with fully useable example workflows,
data loading scripts, etc.
