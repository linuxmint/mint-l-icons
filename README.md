
Credits
=======

The application and category icons originate from the Moka icon theme:
	Link: https://github.com/moka-project/moka-icon-theme
	Author: Sam Hewitt <hewittsamuel@gmail.com>
	License: Creative Commons Attribution-ShareAlike 4.0 (https://creativecommons.org/licenses/by-sa/4.0)

The mimetypes icons originate from the Papirus icon theme:
	Link: https://github.com/varlesh/papirus-suite
	Author: Alexey Varfolomeev
	License: Creative Commons Attribution-ShareAlike 4.0 (https://creativecommons.org/licenses/by-sa/4.0)

which itself is based on the Paper icon theme:
	Link: https://github.com/snwh/paper-icon-theme
	Author: Sam Hewitt <hewittsamuel@gmail.com>
	License: Creative Commons Attribution-ShareAlike 4.0 (https://creativecommons.org/licenses/by-sa/4.0)

License
=======

This theme is licensed under Creative Commons Attribution-ShareAlike 4.0 (https://creativecommons.org/licenses/by-sa/4.0).

Any bundled software is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3, or (at your option) any later version.

Useful commands
===============

To find circular symbolic links:

	find . -follow -printf ""

To find broken links:

	find -L usr/ -type l

To find files with spaces in their filenames (that breaks the icon cache generation):

	find . | egrep '. '
