| [MainPage](MainPage.md) | [Using](Using.md) | [Download](Download.md) | FAQ | [Screenshots](Screenshots.md) |

  * **Why avr32fs ?**
After playing with build script provided by Atmel and with python script provided by Correa I spent some days thinking how to obtain a flexible tool for creating the root files system. In Linux From Scratch (LFS) page I found nALFS, a program used to build LFS projects. nAFLS builds an entire system just using rules that comes from XML files. Although I am not a big XML enthusiast, nAFLS seemed flexible enough for creating the root file system. Moreover, I think it is simple to modify/extend and it has a good console interface (good log, compilation progress, and so on).

Using nALFS, I created an initial set of XML files for building an NGW100 image (just linux, dropbear, zlib, uclib and busybox). With some modifications it can be used for STK1000 as well.

Before my own solution, I tried latest buildroot (compilation problems for avr32) and T2 (problems as well, not solved by T2 team yet, according to some emails I exchange with the team).

T2 sounds interesting, with more diagnostics and better command line options than buidroot. However, since both didn't work for me, I decided to fix all problems in Atmel scripts (my board is NGW100, we have a long thread about this in this forum). After doing this, I could see that Atmel scripts are very near of LFS, changing only the language (shell x xml) and making modifications and extension easy when using LFS.

avr32fs does not compare directly with T2/buildroot but with Atmel scripts. T2/buildroot will compile all required tools but they don't solve the customization phase (for instance, startup and etc customization). You need to do it by hand and keep your modification using some alternative method. With LFS (and avr32fs) strategy, you can determine what/how /which/when thinks will be compiled and, additionally, you can specify your customizations, inside the same framework. And, ok, I am lazy and would like to call a program and just wait for my image file, while taking a great Brazilian coffee :-)

Although T2 proposal is really nice, I think that when using avr32fs we have flexibility but without losing control over what is happening (no black boxes).
For instance, if you decide to change fstab, just copy stage1/etcfiles.xml (e.g., to myetcfiles.xml) and change which files are included in ngw.xml (etcfiles.xml -> myetcfiles.xml) . If you need other complete skeleton, copy skel/ngw and set the new skel inside config/general.ent. You can do it using Atmel build script, but debugging, progress visualization and changeability are increased when nAFLS is employed.

Take a look at nAFLS interface and you understand what I am saying when you start to browse the project nodes.
  * **Who ?**
My name is Marcelo Barros de Almeida. I am interested in embedded Linux, networking administration, Linux servers, Pyhton and C programming. I received BS in Electrical Engineering at UNIFEI (Itajubá/MG - Brazil, 1996) and master/doctor degrees at Federal University of Minas Gerais (Belo Horizonte/MG - Brazil, 1998 and 2002 respectively). At that time, my research was related to intelligence computational, including support vector machines and neural networks. Currently, I am working as a research and development electrical engineer at Smar Equipamentos Industriais LTDA, located at Sertãozinho/SP - Brazil.