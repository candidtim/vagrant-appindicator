# Copyright 2014, candidtim (https://github.com/candidtim)
#
# This file is part of Vagrant AppIndicator for Ubuntu.
#
# Vagrant AppIndicator for Ubuntu is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Foobar.
# If not, see <http://www.gnu.org/licenses/>.


from gi.repository import Gdk as gdk


THEME_DARK = "dark"
THEME_LIGHT = "light"


def _luminance(r, g, b, base=256):
    """Calculates luminance of a color, on a scale from 0 to 1, meaning that 1 is the highest luminance.
    r, g, b arguments values should be in 0..256 limits, or base argument should define the upper limit otherwise"""
    return (0.2126*r + 0.7152*g + 0.0722*b)/base


def __pixel_at(x, y):
    """Returns (r, g, b) color code for a pixel with given coordinates (each value is in 0..256 limits)"""
    root_window = gdk.get_default_root_window()
    buf = gdk.pixbuf_get_from_window(root_window, x, y, 1, 1)
    pixels = buf.get_pixels()
    if type(pixels) == type(""):
        rgb = tuple([int(byte.encode('hex'), 16) for byte in pixels])
    else:
        rgb = tuple(pixels)
    return rgb


def _get_theme():
    """Returns one of THEME_LIGHT or THEME_DARK, corresponding to current user's UI theme"""
    # getting color of a pixel on a top bar, and identifying best-fitting color theme based on its luminance
    pixel_rgb = __pixel_at(2, 2)
    luminance = _luminance(*pixel_rgb)
    return THEME_LIGHT if luminance >= 0.5 else THEME_DARK


THEME = _get_theme()
