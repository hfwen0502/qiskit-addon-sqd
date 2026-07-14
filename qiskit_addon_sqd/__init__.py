# This code is a Qiskit project.
#
# (C) Copyright IBM 2024.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# Warning: this module is not documented and it does not have an RST file.
# If we ever publicly expose interfaces users can import from this module,
# we should set up its RST file.
"""Primary SQD functionality."""

__all__ = ["enable_engine"]


def __getattr__(name):
    # Lazily expose ``qiskit_addon_sqd.enable_engine`` without importing the
    # heavy ``fermion`` module (pyscf/jax) at ``import qiskit_addon_sqd`` time.
    # PEP 562 module-level __getattr__.
    if name == "enable_engine":
        from .fermion import enable_engine

        return enable_engine
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
