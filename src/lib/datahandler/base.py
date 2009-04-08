#
# Revelation - a password manager for GNOME 2
# http://oss.codepoet.no/revelation/
# $Id: base.py 602 2007-01-03 08:06:28Z erikg $
#
# Module for basic datahandler functionality
#
#
# Copyright (c) 2003-2006 Erik Grinaker
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#

class Error(Exception):
	"Base exception for data handler"
	pass

class DataError(Error):
	"Exception for invalid data"
	pass

class FormatError(Error):
	"Exception for invalid file formats"
	pass

class PasswordError(Error):
	"Exception for wrong password"
	pass

class VersionError(Error):
	"Exception for unknown versions"
	pass



class DataHandler(object):
	"A datahandler base class, real datahandlers are subclassed from this"

	name		= None
	importer	= False
	exporter	= False
	encryption	= False


	def __init__(self):
		pass


	def check(self, input):
		"Fallback method, subclasses should override this"

		pass


	def detect(self, input):
		"Fallback method, subclasses should override this"

		return False


	def export_data(self, entrystore, password):
		"Fallback method, subclasses should override this"

		return ""


	def import_data(self, input, password):
		"Fallback method, subclasses should override this"

		pass

