# **************************************************************************
# *
# * Authors: Yunior C. Fonseca Reyna    (cfonseca@cnb.csic.es)
# *
# *
# * Unidad de  Bioinformatica of Centro Nacional de Biotecnologia , CSIC
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************
import pyworkflow.viewer as pwviewer
import pyworkflow.utils as pwutils

import tomo.objects
import sphire.convert
from sphire import NAPARI_VIEWER_CBOX_FILES


class NapariViewer(pwviewer.Viewer):
    """ Wrapper to visualize 3D coordinates using napari boxmanager
    """
    _environments = [pwviewer.DESKTOP_TKINTER]
    _targets = [tomo.objects.SetOfCoordinates3D]
    _name = "Napari"

    def __init__(self, **kwargs):
        pwviewer.Viewer.__init__(self, **kwargs)
        self._views = []

    def _visualize(self, obj, **kwargs):
        views = []
        cls = type(obj)

        if issubclass(cls, tomo.objects.SetOfCoordinates3D):
            from .views_tkinter_tree import SphireGenericView
            self.generateCboxFiles(obj.getPrecedents(), obj)
            setCoord3DView = SphireGenericView(self.getTkRoot(), self.protocol,
                                               obj.getPrecedents(),
                                               isInteractive=True,
                                               itemDoubleClick=True)
            views.append(setCoord3DView)

        return views

    def generateCboxFiles(self, tomograms, coordinates3D):
        """ Converts a set of coordinates to box files and binaries to mrc.
        It generates 2 folders: one for the box files and another for
        the mrc files.
        """
        inputTomos = tomograms
        coordSet = coordinates3D

        path = self.protocol._getExtraPath(NAPARI_VIEWER_CBOX_FILES)
        pwutils.makePath(path)

        tomoList = [tomo.clone() for tomo in inputTomos]
        sphire.convert.writeSetOfCoordinates3D(path, coordSet, tomoList)
