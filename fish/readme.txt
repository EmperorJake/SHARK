--- THIS README NEEDS RE-WRITING :o ---

Lantau [Ferry]                Introduced: 1860; Speed: 20.0mphJohann Strauss [Paddle Steamer]  Introduced: 1860; Speed: 20.0mphWellfleet [Trawler]           Introduced: 1860; Speed: 18.0mphHarbour Point [Utility Vessel]  Introduced: 1860; Speed: 19.0mphMalin [Freighter]             Introduced: 1860; Speed: 18.0mphFinisterre [Freighter]        Introduced: 1860; Speed: 18.0mphWhitgift [Freight Barge]      Introduced: 1860; Speed: 18.0mphSaint Marie [Barge Tug]       Introduced: 1860; Speed: 16.0mphFreshney [Tanker Barge]       Introduced: 1870; Speed: 18.0mphFrisco Bay [Freighter]        Introduced: 1875; Speed: 18.0mphLittle Cumbrae [Freighter]    Introduced: 1885; Speed: 20.0mphConstance [Freight Barge]     Introduced: 1885; Speed: 18.0mphBanquereau [Ferry]            Introduced: 1890; Speed: 20.0mphAltamira [Freighter]          Introduced: 1890; Speed: 20.0mphQuessant [Freighter]          Introduced: 1895; Speed: 18.0mphFastnet [Paddle Steamer]      Introduced: 1900; Speed: 28.0mphTramp [Steamer]               Introduced: 1900; Speed: 28.0mphOlympic [Log Tug]             Introduced: 1900; Speed: 12.0mphVolgoneft 270 [Tanker Barge]  Introduced: 1900; Speed: 18.0mphTiree [Ferry]                 Introduced: 1917; Speed: 21.0mphGeneva [Freight Barge]        Introduced: 1920; Speed: 16.0mphCastle Point [Tanker]         Introduced: 1920; Speed: 20.0mphVolgoneft 540 [Tanker Barge]  Introduced: 1920; Speed: 18.0mphRoland [Tanker]               Introduced: 1926; Speed: 20.0mphLabrador [Utility Vessel]     Introduced: 1929; Speed: 23.0mphIsland Trader [Blank]         Introduced: 1930; Speed: 30.0mphOran [Freighter]              Introduced: 1930; Speed: 23.0mphJosephine [Trawler]           Introduced: 1933; Speed: 21.0mphShannon [Freighter]           Introduced: 1934; Speed: 23.0mphGrindavik [Reefer]            Introduced: 1934; Speed: 26.0mphRosario [Ferry]               Introduced: 1937; Speed: 23.0mphMcClure [Livestock Ship]      Introduced: 1937; Speed: 26.0mphVolgoneft 320 [Tanker Barge]  Introduced: 1948; Speed: 21.0mphStornoway [Ferry]             Introduced: 1956; Speed: 23.0mphVolgoneft 630 [Tanker Barge]  Introduced: 1956; Speed: 21.0mphKlyazma [Hydrofoil]           Introduced: 1957; Speed: 45.0mphMaddalena [Ferry]             Introduced: 1959; Speed: 23.0mphConnor Freight [Ferry]        Introduced: 1960; Speed: 30.0mphCadiz [Freighter]             Introduced: 1963; Speed: 26.0mphHelsinki [Reefer]             Introduced: 1963; Speed: 30.0mphNanaimo 70 [Hovercraft]       Introduced: 1965; Speed: 70.0mphProvence Edibles [Tanker]     Introduced: 1965; Speed: 26.0mphSantorini [Freighter]         Introduced: 1966; Speed: 26.0mphPegwell Super 4 [Hovercraft]  Introduced: 1968; Speed: 70.0mphMeteor [Freighter]            Introduced: 1968; Speed: 26.0mphMarstein [Freighter]          Introduced: 1968; Speed: 26.0mphHitsuji [Livestock Ship]      Introduced: 1969; Speed: 30.0mphKwangtung [Trawler]           Introduced: 1972; Speed: 30.0mphOhshima Freight [Hovercraft]  Introduced: 1972; Speed: 46.0mphHammerhead [Ferry]            Introduced: 1973; Speed: 30.0mphYokohama [Tanker]             Introduced: 1973; Speed: 26.0mphMatsushima [Hydrofoil]        Introduced: 1978; Speed: 56.0mphNieuwpoort [Container Feeder]  Introduced: 1979; Speed: 30.0mphHuanghai LNG [Tanker]         Introduced: 1982; Speed: 30.0mphMaspalomas [Freighter]        Introduced: 1988; Speed: 30.0mphSan Juan [Ferry]              Introduced: 1990; Speed: 30.0mphDieze [Container Barge]       Introduced: 1990; Speed: 25.0mphEnoshima [Catamaran]          Introduced: 1997; Speed: 50.0mphMount Blaze [Fast Ferry]      Introduced: 2008; Speed: 60.0mph

My Fancy NewGRF Name
-----------------------------------

Contents:

1 About
2 Usage and Parameters
3 Building from source
  3.1 Speed issues
  3.2 Obtaining the source
4 Credits
5 License



-------
1 About
-------

This is a NewGRF

Name of this Repo:  Example NewGRF project
Repository version: {{REPO_REVISION}}



----------------------
2 Usage and Parameters
----------------------



----------------------
3 Building from source
----------------------

Usually there's not much which needs to be changed when you obtain the
source. Your friends will usually be
    make
	make install
Both will build the grf from source, the latter will also try to copy
the grf into your grf folder so that it is available for testing and
use straight away.

A brief overview over all Makefile targets is given here:

all:
	This is the default target, if also no parameter is given to
	make. It will simply build the grf file, if it needs building

depend:
	Re-run the dependency check. Usually not manually needed.

docs:
	Build the documentation files

bundle:
	This target will create a directory called "<name>-nightly" and
	copy the grf file there and the documentation files, readme.txt,
	changelog.txt and license.txt

bundle_zip
	This will zip the bundle directory into one zip for distribution

bundle_tar
	This will tar the bundle directory into a tar archive for
	distribution or upload to bananas

bundle_src
	Creates a source bundle

install:
	This will create a tar archive (like bundle_tar) and copy it
	into the INSTALLDIR as specified in Makefile.local (or the
	default dir, if that isn't defined). Don't rely on a good
	detection of the default installation directory. It's
	especially bound to fail on windows machines.

distclean:
	This phony target cleans everything from a source bundle which
	wasn't shipped.

clean:
	This phony target will delete all files which this Makefile will
	create

mrproper:
	This phony target will delete also all directories created by
	different Makefile targets

remake:
	It's a shortcut for first cleaning the dir and then making the
	grf anew.

addcheck:
	Check whether there are some files required but not part of the
	repository.

check:
	Check the md5sum of the built newgrf against the supplied md5sum
	(Intended to be used when building from tar balls)


3.1 Speed issues
----------------

A note concerning the speed of the makefile:
It seems that the required tools using MinGW and / or msys are thoroughly
slow on windows. A few example run times for OpenGFX, same processor type
(both core 2 duo, 2.26GHz for the windows machine, 2.0 GHz for the OSX
machine). Note that the values given are the 'real' time. Even though
this varies more and is dependent on the processor load, that's what you
have to wait for; the 'user' times are quite low on the windows machine
(~16s), but that by no means reflects the build time. Times are from
OpenGFX r539 with makefile r199.

DEP_CHECK_TYPE         windows               bash native
                 native       in VM            (OSX)
none            1m23.360s      -             0m32.781s
mdep            1m54.484s   0m30.164s        0m33.807s
normal          2m37.857s      -             0m36.528s


3.2 Obtaining the source
------------------------

The source code can be obtained from the #openttdcoop DevZone at
    http://dev.openttdcoop.org/projects/newgrf-makefile
or via mercurial checkout
    hg clone http://hg.openttdcoop.org/newgrf-makefile



---------
4 Credits
---------

Author: Ingo von Borstel (aka planetmaker)

Special thanks to #openttdcoop and especially Ammler who provides and
works a lot on maintaining the Development Zone where this repository is
hosted and who also frequently gives much valuable input. Thanks also to
Alberth, Terkhen Yexo, Rubidium and Ammler who frequently give valuable
input in form of advice and patches to this project. Last but not least
thanks to all the NewGRF authors whose NewGRFs can be my playground for
this project.



--------------
5 License
--------------

My Fancy NewGRF
Copyright (C) 2011 planetmaker and others

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this NewGRF; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
