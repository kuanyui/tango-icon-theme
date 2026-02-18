# Tango Icon Theme

![](tango-logo.svg)

A modest renaissance of [Freedesktop's Tango Desktop Project](https://en.wikipedia.org/wiki/Tango_Desktop_Project).

This is a fork from [sebkur/tango-icon-theme](http://github.com/sebkur/tango-icon-theme).

> # ![](48x48/places/start-here.svg) Origin
> This was a long process of digital archaeology...
>
> 1. [tango-icon-theme-0.8.90.tar.bz2](http://tango.freedesktop.org/releases/tango-icon-theme-0.8.90.tar.bz2) final release available on freedesktop.org, **but it provides PNG only, except 48x48 are in SVG**. The official site of Freedesktop Tango Project has already been down... This URL is found in [AUR](https://aur.archlinux.org/packages/tango-icon-theme)...
> 2. Git repo ([cgit](https://cgit.freedesktop.org/tango/tango-icon-theme/), [gitlab](https://gitlab.freedesktop.org/tango/tango-icon-theme)) can be found in [freedesktop](https://cgit.freedesktop.org/), **but it lacks lots of original Tango icons... It looks more like... a draft of `gnome-icon-theme`**. Maybe it was faults of the administrators of freedesktop.org when migrating CVS server into git repo, mistakenly excluded lots of old SVG source code... Argh.
> 3. **Fortunately, [Debian's package server](https://tracker.debian.org/pkg/tango-icon-theme) still** remains a full (I guess) snapshot of source code and VCS ([src pkg](https://sources.debian.org/src/tango-icon-theme/0.9.0-1), [git](https://git.golem.linux.it/matteobin/tango-icon-theme)), contains many useful SVG files! Heritage of forgotten ancient civilizations! **Thank you Debian!**
>   - However, the source code git repo I found on Debian already contains only 1 initial commit... No commit history is preserved... But its `README.md` described:
>     > This is a fork of Tango icon theme based on the 0.8.90-11 version of the Debian package and this Git repository <https://github.com/sebkur/tango-icon-theme>, to add XDG user directory icons, PDF MIME type icon, restore the missing scalable mail-mark-not-junk.svg icon from 0.8.90, and include some Debian patches. Tango icon theme was forked because upstream is dead.
> 4. **At last**, I found [sebkur/tango-icon-theme](http://github.com/sebkur/tango-icon-theme) still preserves commit history, so **I decide to fork it**. (out of nostalgia, respect to the original authors, and as records of the history of the Linux desktop in the 2000s.)

# ![](48x48/apps/help-browser.svg) Why Fork?

Maintenance of the original version of `tango-icon-theme` has been discontinued, and was relicensed from CC-BY-SA 2.5 into the Public Domain (as stated in the [0.8.90 tarball](http://tango.freedesktop.org/releases/tango-icon-theme-0.8.90.tar.bz2)) on [2009-02-26](https://tango.freedesktop.org/releases/) by original authors, **"Tango Desktop Project contributors from freedesktop.org"**.

I love Tango Icons, and I don't want this wonderful icon theme and these great authors be forgotten in the tide of an era dominated by flat design. So I forked `tango-icon-theme`, try to keep the spirit and legacy of "Tango Desktop Project" alive.

## Differences against the vanilla version

- Lots of source file of Tango Icon Theme is already `*.xcf` instead of `*.svg`, so if I have time, they may be (slowly) re-drawn to SVG manually...
- `scalable/` is renamed to `48x48/` because they are really 48x48.
- Draw more icons.
- As an alternative of Ubuntu Humanity or GNOME Icon Theme, especially for the compatibility of GPLv2/v3, the mainstream licenses of Linux GUI applications.

# ![](48x48/mimetypes/application-certificate.svg) License

Copyright (c) 2005-2009, 2021, 2026. freedesktop.org Tango Desktop Project contributors.

This project is dual-licensed under the terms of the GNU General Public License version 2 or version 3 (in your option); the "any later version" clause does NOT apply. See [LICENSES/GPL-2.0-only.txt](LICENSES/GPL-2.0-only.txt) and [LICENSES/GPL-3.0-only.txt](LICENSES/GPL-3.0-only.txt) for the full text.

This choice was made to maximize compatibility with GPL-licensed GUI applications (mainstream in FLOSS GUI applications) and to lower the barrier for contribution. Thanks for your understanding.

> [!NOTE]
> ### Credits
> After all, one of a goal I forked `tango-icon-theme` is to make Tango Desktop Project not to be forgotten. Therefore, while GPLv2 and GPLv3 licenses do not permit adding extra obligations, **we would greatly appreciate it if you choose to credit the original authors `Tango Desktop Project contributors from freedesktop.org` in your project**, either in about UI, documentation, or acknowledgements.
>
> This is a voluntary request and has **no** effect on your rights under the GPL.

------

# Original README from [sebkur/tango-icon-theme](http://github.com/sebkur/tango-icon-theme)

This is an icon theme that follows the [Tango visual guidelines][1]. Currently
it depends on Imagemagick for creation of 24x24 bitmaps by adding a 1px padding
around the 22x22px version. For GNOME and KDE you will also need
icon-naming-utils that allow the theme to work in these environments before
they follow [the new naming scheme][2].

## Information about the Tango icons elsewhere on the web

There's a [Wikipedia article][3]. Also Wikimedia Commons has
[a page][4] about the icons that includes more icons than the ones
available in this repository.
The [Gnome desktop icons] are also similar but contains more and
partially different icons than Tango.

[1]: http://tango.freedesktop.org/Tango_Icon_Theme_Guidelines
[2]: http://tango.freedesktop.org/Standard_Icon_Naming_Specification
[3]: https://en.wikipedia.org/wiki/Tango_Desktop_Project
[4]: https://commons.wikimedia.org/wiki/Tango_icons
[5]: https://commons.wikimedia.org/wiki/GNOME_Desktop_icons

## actions
![](48x48/actions/address-book-new.svg)
![](48x48/actions/appointment-new.svg)
![](48x48/actions/bookmark-new.svg)
![](48x48/actions/contact-new.svg)
![](48x48/actions/document-new.svg)
![](48x48/actions/document-open.svg)
![](48x48/actions/document-print-preview.svg)
![](48x48/actions/document-print.svg)
![](48x48/actions/document-properties.svg)
![](48x48/actions/document-save-as.svg)
![](48x48/actions/document-save.svg)
![](48x48/actions/edit-clear.svg)
![](48x48/actions/edit-copy.svg)
![](48x48/actions/edit-cut.svg)
![](48x48/actions/edit-delete.svg)
![](48x48/actions/edit-find-replace.svg)
![](48x48/actions/edit-find.svg)
![](48x48/actions/edit-paste.svg)
![](48x48/actions/edit-redo.svg)
![](48x48/actions/edit-select-all.svg)
![](48x48/actions/edit-undo.svg)
![](48x48/actions/folder-new.svg)
![](48x48/actions/format-indent-less.svg)
![](48x48/actions/format-indent-more.svg)
![](48x48/actions/format-justify-center.svg)
![](48x48/actions/format-justify-fill.svg)
![](48x48/actions/format-justify-left.svg)
![](48x48/actions/format-justify-right.svg)
![](48x48/actions/format-text-bold.svg)
![](48x48/actions/format-text-italic.svg)
![](48x48/actions/format-text-strikethrough.svg)
![](48x48/actions/format-text-underline.svg)
![](48x48/actions/go-bottom.svg)
![](48x48/actions/go-down.svg)
![](48x48/actions/go-first.svg)
![](48x48/actions/go-home.svg)
![](48x48/actions/go-jump.svg)
![](48x48/actions/go-last.svg)
![](48x48/actions/go-next.svg)
![](48x48/actions/go-previous.svg)
![](48x48/actions/go-top.svg)
![](48x48/actions/go-up.svg)
![](48x48/actions/list-add.svg)
![](48x48/actions/list-remove.svg)
![](48x48/actions/mail-forward.svg)
![](48x48/actions/mail-mark-junk.svg)
![](48x48/actions/mail-mark-not-junk.svg)
![](48x48/actions/mail-message-new.svg)
![](48x48/actions/mail-reply-all.svg)
![](48x48/actions/mail-reply-sender.svg)
![](48x48/actions/mail-send-receive.svg)
![](48x48/actions/media-eject.svg)
![](48x48/actions/media-playback-pause.svg)
![](48x48/actions/media-playback-start.svg)
![](48x48/actions/media-playback-stop.svg)
![](48x48/actions/media-record.svg)
![](48x48/actions/media-seek-backward.svg)
![](48x48/actions/media-seek-forward.svg)
![](48x48/actions/media-skip-backward.svg)
![](48x48/actions/media-skip-forward.svg)
![](48x48/actions/process-stop.svg)
![](48x48/actions/system-lock-screen.svg)
![](48x48/actions/system-log-out.svg)
![](48x48/actions/system-search.svg)
![](48x48/actions/system-shutdown.svg)
![](48x48/actions/tab-new.svg)
![](48x48/actions/view-fullscreen.svg)
![](48x48/actions/view-refresh.svg)
![](48x48/actions/window-new.svg)

## apps
![](48x48/apps/accessories-calculator.svg)
![](48x48/apps/accessories-character-map.svg)
![](48x48/apps/accessories-text-editor.svg)
![](48x48/apps/help-browser.svg)
![](48x48/apps/internet-group-chat.svg)
![](48x48/apps/internet-mail.svg)
![](48x48/apps/internet-news-reader.svg)
![](48x48/apps/internet-web-browser.svg)
![](48x48/apps/office-calendar.svg)
![](48x48/apps/preferences-desktop-accessibility.svg)
![](48x48/apps/preferences-desktop-assistive-technology.svg)
![](48x48/apps/preferences-desktop-font.svg)
![](48x48/apps/preferences-desktop-keyboard-shortcuts.svg)
![](48x48/apps/preferences-desktop-locale.svg)
![](48x48/apps/preferences-desktop-multimedia.svg)
![](48x48/apps/preferences-desktop-remote-desktop.svg)
![](48x48/apps/preferences-desktop-screensaver.svg)
![](48x48/apps/preferences-desktop-theme.svg)
![](48x48/apps/preferences-desktop-wallpaper.svg)
![](48x48/apps/preferences-system-network-proxy.svg)
![](48x48/apps/preferences-system-session.svg)
![](48x48/apps/preferences-system-windows.svg)
![](48x48/apps/system-file-manager.svg)
![](48x48/apps/system-installer.svg)
![](48x48/apps/system-software-update.svg)
![](48x48/apps/system-users.svg)
![](48x48/apps/utilities-system-monitor.svg)
![](48x48/apps/utilities-terminal.svg)

## categories
![](48x48/categories/applications-accessories.svg)
![](48x48/categories/applications-development.svg)
![](48x48/categories/applications-games.svg)
![](48x48/categories/applications-graphics.svg)
![](48x48/categories/applications-internet.svg)
![](48x48/categories/applications-multimedia.svg)
![](48x48/categories/applications-office.svg)
![](48x48/categories/applications-other.svg)
![](48x48/categories/applications-system.svg)
![](48x48/categories/preferences-desktop-peripherals.svg)
![](48x48/categories/preferences-desktop.svg)
![](48x48/categories/preferences-system.svg)

## devices
![](48x48/devices/audio-card.svg)
![](48x48/devices/audio-input-microphone.svg)
![](48x48/devices/battery.svg)
![](48x48/devices/camera-photo.svg)
![](48x48/devices/camera-video.svg)
![](48x48/devices/computer.svg)
![](48x48/devices/drive-harddisk.svg)
![](48x48/devices/drive-optical.svg)
![](48x48/devices/drive-removable-media.svg)
![](48x48/devices/input-gaming.svg)
![](48x48/devices/input-keyboard.svg)
![](48x48/devices/input-mouse.svg)
![](48x48/devices/media-flash.svg)
![](48x48/devices/media-floppy.svg)
![](48x48/devices/media-optical.svg)
![](48x48/devices/multimedia-player.svg)
![](48x48/devices/network-wired.svg)
![](48x48/devices/network-wireless.svg)
![](48x48/devices/printer.svg)
![](48x48/devices/video-display.svg)

## emblems
![](48x48/emblems/emblem-favorite.svg)
![](48x48/emblems/emblem-important.svg)
![](48x48/emblems/emblem-photos.svg)
![](48x48/emblems/emblem-readonly.svg)
![](48x48/emblems/emblem-symbolic-link.svg)
![](48x48/emblems/emblem-system.svg)
![](48x48/emblems/emblem-unreadable.svg)

## emotes
![](48x48/emotes/face-angel.svg)
![](48x48/emotes/face-cool.svg)
![](48x48/emotes/face-crying.svg)
![](48x48/emotes/face-devilish.svg)
![](48x48/emotes/face-glasses.svg)
![](48x48/emotes/face-grin.svg)
![](48x48/emotes/face-kiss.svg)
![](48x48/emotes/face-monkey.svg)
![](48x48/emotes/face-plain.svg)
![](48x48/emotes/face-sad.svg)
![](48x48/emotes/face-smile-big.svg)
![](48x48/emotes/face-smile.svg)
![](48x48/emotes/face-surprise.svg)
![](48x48/emotes/face-wink.svg)

## mimetypes
![](48x48/mimetypes/application-certificate.svg)
![](48x48/mimetypes/application-x-executable.svg)
![](48x48/mimetypes/audio-x-generic.svg)
![](48x48/mimetypes/font-x-generic.svg)
![](48x48/mimetypes/image-x-generic.svg)
![](48x48/mimetypes/package-x-generic.svg)
![](48x48/mimetypes/text-html.svg)
![](48x48/mimetypes/text-x-generic-template.svg)
![](48x48/mimetypes/text-x-generic.svg)
![](48x48/mimetypes/text-x-script.svg)
![](48x48/mimetypes/video-x-generic.svg)
![](48x48/mimetypes/x-office-address-book.svg)
![](48x48/mimetypes/x-office-calendar.svg)
![](48x48/mimetypes/x-office-document-template.svg)
![](48x48/mimetypes/x-office-document.svg)
![](48x48/mimetypes/x-office-drawing-template.svg)
![](48x48/mimetypes/x-office-drawing.svg)
![](48x48/mimetypes/x-office-presentation-template.svg)
![](48x48/mimetypes/x-office-presentation.svg)
![](48x48/mimetypes/x-office-spreadsheet-template.svg)
![](48x48/mimetypes/x-office-spreadsheet.svg)

## misc
![](48x48/misc/appointment.svg)
![](48x48/misc/bookmark.svg)
![](48x48/misc/contact.svg)
![](48x48/misc/document.svg)
![](48x48/misc/mail-message.svg)
![](48x48/misc/password-preferences.svg)
![](48x48/misc/tab.svg)
![](48x48/misc/window.svg)

## places
![](48x48/places/folder-remote.svg)
![](48x48/places/folder-saved-search.svg)
![](48x48/places/folder.svg)
![](48x48/places/network-server.svg)
![](48x48/places/network-workgroup.svg)
![](48x48/places/start-here.svg)
![](48x48/places/user-desktop.svg)
![](48x48/places/user-home.svg)
![](48x48/places/user-trash.svg)

## status
![](48x48/status/audio-volume-high.svg)
![](48x48/status/audio-volume-low.svg)
![](48x48/status/audio-volume-medium.svg)
![](48x48/status/audio-volume-muted.svg)
![](48x48/status/battery-caution.svg)
![](48x48/status/dialog-error.svg)
![](48x48/status/dialog-information.svg)
![](48x48/status/dialog-warning.svg)
![](48x48/status/folder-drag-accept.svg)
![](48x48/status/folder-open.svg)
![](48x48/status/folder-visiting.svg)
![](48x48/status/image-loading.svg)
![](48x48/status/image-missing.svg)
![](48x48/status/mail-attachment.svg)
![](48x48/status/network-error.svg)
![](48x48/status/network-idle.svg)
![](48x48/status/network-offline.svg)
![](48x48/status/network-receive.svg)
![](48x48/status/network-transmit-receive.svg)
![](48x48/status/network-transmit.svg)
![](48x48/status/network-wireless-encrypted.svg)
![](48x48/status/printer-error.svg)
![](48x48/status/software-update-available.svg)
![](48x48/status/software-update-urgent.svg)
![](48x48/status/user-trash-full.svg)
![](48x48/status/weather-clear-night.svg)
![](48x48/status/weather-clear.svg)
![](48x48/status/weather-few-clouds-night.svg)
![](48x48/status/weather-few-clouds.svg)
![](48x48/status/weather-overcast.svg)
![](48x48/status/weather-severe-alert.svg)
![](48x48/status/weather-showers-scattered.svg)
![](48x48/status/weather-showers.svg)
![](48x48/status/weather-snow.svg)
![](48x48/status/weather-storm.svg)
