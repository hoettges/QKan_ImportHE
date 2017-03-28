# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ImportFromHE
                                 A QGIS plugin
 Importiert Kanaldaten aus Hystem-Extran
                             -------------------
        begin                : 2016-10-06
        copyright            : (C) 2016 by Jörg Höttges/FH Aachen
        email                : hoettges@fh-aachen.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

import logging, site, os.path
from datetime import datetime as dt

# Aufsetzen des Logging-Systems
logger = logging.getLogger('QKan_Laengsschnitt')
formatter = logging.Formatter('%(asctime)s %(name)s-%(levelname)s: %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)

dnam = dt.today().strftime("%Y%m%d")
fnam = os.path.join(site.getuserbase(),'QKan_Laengsschnitt{}.log'.format(dnam))
fh = logging.FileHandler(fnam)
fh.setFormatter(formatter)
logger.addHandler(fh)

# Warnlevel setzten
logger.setLevel(logging.DEBUG)
ch.setLevel(logging.ERROR)
fh.setLevel(logging.DEBUG)


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ImportFromHE class from file ImportFromHE.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .k_he2qk import ImportFromHE
    return ImportFromHE(iface)
