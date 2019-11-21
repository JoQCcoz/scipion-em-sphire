# -*- coding: utf-8 -*
# **************************************************************************
# *
# * Authors:    Peter Horvath [1]
# *             Pablo Conesa  [1]
# *             J.M. De la Rosa Trevin (delarosatrevin@scilifelab.se) [2]
# *             Jorge Jiménez [1]
# *
# *
# * [1] Unidad de  Bioinformatica of Centro Nacional de Biotecnologia , CSIC
# * [2] SciLifeLab, Stockholm University
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

# we declare global constants to multiple usage
import os

# crYOLO ###############################################################################################################

def getCryoloEnvName(version):
    return "cryolo-%s" % version

V1_5_3 = "1.5.3"
V1_5_4_rc3 = "1.5.4.rc3"
VERSIONS = [V1_5_3, V1_5_4_rc3]

DEFAULT_ENV_NAME = getCryoloEnvName(V1_5_3)
DEFAULT_ACTIVATION_CMD = 'conda activate ' + DEFAULT_ENV_NAME
CRYOLO_ENV_ACTIVATION = 'CRYOLO_ENV_ACTIVATION'
CRYOLO_GENMOD_VAR = 'CRYOLO_GENERIC_MODEL'
CONDA_ACTIVATION_CMD_VAR = 'CONDA_ACTIVATION_CMD'

CRYOLO_GENMOD = 'cryolo_model'
# Model constants


def _modelFn(modelKey):
    return 'gmodel_phosnet_%s.h5' % modelKey

CRYOLO_GENMOD_20190516 = '20190516'
CRYOLO_GENMOD_20190516_FN = _modelFn(CRYOLO_GENMOD_20190516)

CRYOLO_GENMOD_201909 = '201909'
CRYOLO_GENMOD_201909_FN = _modelFn(CRYOLO_GENMOD_201909)

# Default model (latest usually)
CRYOLO_GENMOD_DEFAULT = os.path.join(CRYOLO_GENMOD + "-" + CRYOLO_GENMOD_201909, CRYOLO_GENMOD_201909_FN)

# crYOLO supported input formats for micrographs
CRYOLO_SUPPORTED_FORMATS = [".mrc", ".tif", ".tiff", ".jpg"]

# Input options for the training model
INPUT_MODEL_GENERAL = 0
INPUT_MODEL_OTHER = 1

# JANNI ################################################################################################################

# Model
def _janniModelFn(modelKey):
    return 'gmodel_janni_{}.h5'.format(modelKey)

JANNI_GENMOD_VAR = 'JANNI_GENERIC_MODEL'
JANNI_GENMOD = "janni_model"  # Name
JANNI_GENMOD_20190703 = "20190703"  # Version
JANNI_GENMOD_20190703_FN = _janniModelFn(JANNI_GENMOD_20190703)  # File name with extension
JANNI_GENMOD_DEFAULT = os.path.join("{}-{}".format(JANNI_GENMOD, JANNI_GENMOD_20190703), JANNI_GENMOD_20190703_FN)

