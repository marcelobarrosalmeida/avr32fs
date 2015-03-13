| [MainPage](MainPage.md) | Using | [Download](Download.md) | [FAQ](FAQ.md) | [Screenshots](Screenshots.md) |

### Before using avr32fs ###

  * Install nALFS. The current profile was tested  using nALFS 1.2.6, downloaded from: http://www.linuxfromscratch.org/alfs/downloads/stable/nALFS-1.2.6.tar.bz2
  * A copy of directory software, provided by Atmel in NGW100 BSP CD is necessary. It was used the following ISO image: http://www.atmel.com/dyn/resources/prod_documents/AVR32_Linux_BSP_CD_Image_2.0.0.iso
  * AVR32 GCC compiler must be working properly. Use NGW100 BSP CD for installing it.
  * Install mtd\_utils.

### Configuring avr32fs ###

Open config/general.ent and set the following values:

  * root\_version (your build version)
  * base\_dir: where you checkout avr32fs files
  * root\_dir: where root will be created
  * packages\_dir: where software directory is located
  * build\_dir: temporary location for building packages
  * kernel\_src: if you installed avr32-linux-gcc, this value should be correct

In this version there is only one skel directory. More may appear in future.

### Running avr32fs ###

  * 

<path\_to>

/nALFS  ngw.xml
  * press 's' and 'f' and wait (use '?' for more options)
  * an jffs2 image file will be created at base\_dir

### Limitations ###

  * just some packages supported at this moment (busybox, zlib, dropbear, uclibc and linux). More are coming.
  * just one skel file with some missing etc files (I need to configure better the skel's contents)
  * just generating jffs2 imagem, other can be added soon.
  * sudo is necessary (devices inside /dev/ requires root privileges)
  * poor documentation

### Some technical details ###

  * We have 3 stages now: root structure generation, packages compilation/install, image generation. Files related to each state are placed inside stage[1-3].
  * All packages and its patches are listed inside config/package.ent
  * Scripts/series2xml.py may help conversion from series (patch files list) to xml
  * Read nALFS DTD documentation for creating/modifying xml: http://www.linuxfromscratch.org/alfs/view/dtd/

