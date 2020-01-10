Name:		gssproxy
Version:	0.7.0
Release:	17%{?dist}
Summary:	GSSAPI Proxy

Group:		System Environment/Libraries
License:	MIT
URL:		https://pagure.io/gssproxy
Source0:	https://releases.pagure.org/gssproxy/gssproxy-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%global servicename gssproxy
%global pubconfpath %{_sysconfdir}/gssproxy
%global gpstatedir %{_localstatedir}/lib/gssproxy

### Patches ###
Patch0: Properly-renew-expired-credentials.patch
Patch1: Change-impersonator-check-code.patch
Patch2: Allow-connection-to-self-when-impersonator-set.patch
Patch3: Make-proc-file-failure-loud-but-nonfatal.patch
Patch4: Turn-on-Wextra.patch
Patch5: Fix-unused-variables.patch
Patch6: Fix-mismatched-sign-comparisons.patch
Patch7: Fix-error-checking-on-get_impersonator_fallback.patch
Patch8: Remove-gpm_release_ctx-to-fix-double-unlock.patch
Patch9: Appease-gcc-7-s-fallthrough-detection.patch
Patch10: Fix-memory-leak.patch
Patch11: Fix-most-memory-leaks.patch
Patch12: Fix-segfault-when-no-config-files-are-present.patch
Patch13: Update-systemd-file.patch
Patch14: Fix-error-handling-in-gp_config_from_dir.patch
Patch15: Fix-silent-crash-with-duplicate-config-sections.patch
Patch16: Do-not-call-gpm_grab_sock-twice.patch
Patch17: Fix-error-message-handling-in-gp_config_from_dir.patch
Patch18: Only-empty-FILE-ccaches-when-storing-remote-creds.patch
Patch19: Handle-outdated-encrypted-ccaches.patch
Patch20: Separate-cred-and-ccache-manipulation-in-gpp_store_r.patch
Patch21: Properly-locate-credentials-in-collection-caches-in-.patch
Patch22: Properly-initialize-ccaches-before-storing-into-them.patch
Patch23: Include-header-for-writev.patch
Patch24: Tolerate-NULL-pointers-in-gp_same.patch
Patch25: Add-Client-ID-to-debug-messages.patch
Patch26: client-Switch-to-non-blocking-sockets.patch
Patch27: server-Add-detailed-request-logging.patch
Patch28: Fix-potential-free-of-non-heap-address.patch
Patch29: Prevent-uninitialized-read-in-error-path-of-XDR-cont.patch
Patch30: Simplify-setting-NONBLOCK-on-socket.patch
Patch31: Fix-handling-of-non-EPOLLIN-EPOLLOUT-events.patch
Patch32: Fix-error-handling-in-gpm_send_buffer-gpm_recv_buffe.patch
Patch33: Emit-debug-on-queue-errors.patch
Patch34: Conditionally-reload-kernel-interface-on-SIGHUP.patch

### Dependencies ###

# From rhbz#1458913 and friends
Requires: libini_config >= 1.3.1-28

Requires: krb5-libs >= 1.15
Requires: keyutils-libs
Requires: libverto-module-base
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

# Currently from rhbz#1458850 and friends
Conflicts: selinux-policy < 3.13.1-166.el7.noarch

### Build Dependencies ###

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: coreutils
BuildRequires: docbook-style-xsl
BuildRequires: doxygen
BuildRequires: findutils
BuildRequires: gettext-devel
BuildRequires: keyutils-libs-devel
BuildRequires: krb5-devel >= 1.15
BuildRequires: libini_config-devel >= 1.3.1-28
BuildRequires: libselinux-devel
BuildRequires: libtool
BuildRequires: libverto-devel
BuildRequires: libxml2
BuildRequires: libxslt
BuildRequires: m4
BuildRequires: pkgconfig
BuildRequires: popt-devel
BuildRequires: sed
BuildRequires: systemd-units


%description
A proxy for GSSAPI credential handling


%prep
%setup -q
%patch0 -p2 -b .Properly-renew-expired-credentials
%patch1 -p2 -b .Change-impersonator-check-code
%patch2 -p2 -b .Allow-connection-to-self-when-impersonator-set
%patch3 -p2 -b .Make-proc-file-failure-loud-but-nonfatal
%patch4 -p2 -b .Turn-on-Wextra
%patch5 -p2 -b .Fix-unused-variables
%patch6 -p2 -b .Fix-mismatched-sign-comparisons
%patch7 -p2 -b .Fix-error-checking-on-get_impersonator_fallback
%patch8 -p2 -b .Remove-gpm_release_ctx-to-fix-double-unlock
%patch9 -p2 -b .Appease-gcc-7-s-fallthrough-detection
%patch10 -p2 -b .Fix-memory-leak
%patch11 -p2 -b .Fix-most-memory-leaks
%patch12 -p2 -b .Fix-segfault-when-no-config-files-are-present
%patch13 -p2 -b .Update-systemd-file
%patch14 -p2 -b .Fix-error-handling-in-gp_config_from_dir
%patch15 -p2 -b .Fix-silent-crash-with-duplicate-config-sections
%patch16 -p2 -b .Do-not-call-gpm_grab_sock-twice
%patch17 -p2 -b .Fix-error-message-handling-in-gp_config_from_dir
%patch18 -p2 -b .Only-empty-FILE-ccaches-when-storing-remote-creds
%patch19 -p2 -b .Handle-outdated-encrypted-ccaches
%patch20 -p2 -b .Separate-cred-and-ccache-manipulation-in-gpp_store_r
%patch21 -p2 -b .Properly-locate-credentials-in-collection-caches-in-
%patch22 -p2 -b .Properly-initialize-ccaches-before-storing-into-them
%patch23 -p2 -b .Include-header-for-writev
%patch24 -p2 -b .Tolerate-NULL-pointers-in-gp_same
%patch25 -p2 -b .Add-Client-ID-to-debug-messages
%patch26 -p2 -b .client-Switch-to-non-blocking-sockets
%patch27 -p2 -b .server-Add-detailed-request-logging
%patch28 -p2 -b .Fix-potential-free-of-non-heap-address
%patch29 -p2 -b .Prevent-uninitialized-read-in-error-path-of-XDR-cont
%patch30 -p2 -b .Simplify-setting-NONBLOCK-on-socket
%patch31 -p2 -b .Fix-handling-of-non-EPOLLIN-EPOLLOUT-events
%patch32 -p2 -b .Fix-error-handling-in-gpm_send_buffer-gpm_recv_buffe
%patch33 -p2 -b .Emit-debug-on-queue-errors
%patch34 -p2 -b .Conditionally-reload-kernel-interface-on-SIGHUP

%build
autoreconf -f -i
%configure \
    --with-pubconf-path=%{pubconfpath} \
    --with-initscript=systemd \
    --disable-static \
    --disable-rpath \
    --with-gpp-default-behavior=REMOTE_FIRST \
    CFLAGS="$CFLAGS -fPIE -fstack-protector-all" \
    LDFLAGS="$LDFLAGS -fPIE -pie -Wl,-z,now"
make %{?_smp_mflags} all
make test_proxymech

%install
rm -rf -- "%{buildroot}"
make install DESTDIR=%{buildroot}
rm -f -- %{buildroot}%{_libdir}/gssproxy/proxymech.la
install -d -m755 %{buildroot}%{_sysconfdir}/gssproxy
install -m644 examples/gssproxy.conf %{buildroot}%{_sysconfdir}/gssproxy/gssproxy.conf
install -m644 examples/99-nfs-client.conf %{buildroot}%{_sysconfdir}/gssproxy/99-nfs-client.conf
mkdir -p %{buildroot}%{_sysconfdir}/gss/mech.d
install -m644 examples/mech %{buildroot}%{_sysconfdir}/gss/mech.d/gssproxy.conf
mkdir -p %{buildroot}/var/lib/gssproxy/rcache

%clean
rm -rf -- "%{buildroot}"


%files
%defattr(-,root,root,-)
%doc COPYING
%{_unitdir}/gssproxy.service
%{_sbindir}/gssproxy
%attr(755,root,root) %dir %{pubconfpath}
%attr(755,root,root) %dir %{gpstatedir}
%attr(700,root,root) %dir %{gpstatedir}/clients
%attr(0600,root,root) %config(noreplace) /%{_sysconfdir}/gssproxy/gssproxy.conf
%attr(0600,root,root) %config(noreplace) /%{_sysconfdir}/gssproxy/99-nfs-client.conf
%attr(0644,root,root) %config(noreplace) /%{_sysconfdir}/gss/mech.d/gssproxy.conf
%attr(700,root,root) %dir /var/lib/gssproxy/rcache
%{_libdir}/gssproxy/proxymech.so
%{_mandir}/man5/gssproxy.conf.5*
%{_mandir}/man8/gssproxy.8*
%{_mandir}/man8/gssproxy-mech.8*


%post
%systemd_post gssproxy.service


%preun
%systemd_preun gssproxy.service


%postun
%systemd_postun_with_restart gssproxy.service


%changelog
* Wed Dec 13 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-17
- Conditionally reload kernel interface on SIGHUP
- Resolves: #1507817

* Tue Dec 12 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-16
- Backport epoll() logic
- Resolves: #1507817

* Wed Dec 06 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-15
- Properly initialize ccaches before storing into them
- Resolves: #1488629

* Fri Dec 01 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-14
- Properly locate credentials in collection caches in mechglue
- Resolves: #1488629

* Tue Oct 31 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-13
- Handle outdated encrypted ccaches
- Resolves: #1488629

* Tue Oct 31 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-12
- Handle outdated encrypted ccaches
- Resolves: #1488629

* Mon Oct 30 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-11
- Fix error message handling in gp_config_from_dir()
- Resolves: #1458913

* Fri Oct 27 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-10
- Fix concurrency issue around server socket handling
- Resolves: #1462974

* Tue Oct 17 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-9
- Log useful warning and merge when config file has duplicate sections
- Resolves: #1458913

* Mon Oct 02 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-8
- Add Conflicts: line for old selinux-policy
- Resolves: #1458850

* Thu Sep 21 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-7
- Backport NFS-related gssproxy.service changes
- Resolves: #1326440

* Mon Sep 11 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-6
- Fix segfault when no config files are present
- Resolves: #1451255

* Thu Aug 17 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-5
- Backport hardening improvements
- Resolves: #1462974

* Wed May 31 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-4
- Make proc file failure loud but nonfatal
- Resolves: #1449238

* Tue Mar 28 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-3
- Stop shipping NFS server snippet (nfs-utils takes it instead)
- Resolves: #1379836

* Tue Mar 14 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-2
- Fix credential handling with mod_auth_gssapi that we broke
- Resolves: #1379836

* Fri Mar 10 2017 Robbie Harwood <rharwood@redhat.com> 0.7.0-1
- New upstream version - 0.7.0
- Resolves: #1379836

* Tue Feb 28 2017 Robbie Harwood <rharwood@redhat.com> 0.6.2-4
- Include fixes for NULL-termination
- Resolves: #1379836

* Thu Feb 23 2017 Robbie Harwood <rharwod@redhat.com> 0.6.2-3
- Document debug_level option
- Resolves: #1379836

* Tue Feb 21 2017 Robbie Harwood <rharwood@redhat.com> 0.6.2-2
- Enable running the test suite
- Resolves: #1379836

* Thu Feb 16 2017 Robbie Harwood <rharwood@redhat.com> 0.6.2-1
- Rebase to latest version since we have krb5-1.15
- Resolves: #1379836
- Resolves: #1344518
- Resolves: #1366782
- Resolves: #1379005
- Resolves: #1379482
- Resolves: #1379616
- Resolves: #1380490
- Resolves: #1378600
- Resolves: #1285012
- Resolves: #1333813

* Tue Sep 06 2016 Robbie Harwood <rharwood@redhat.com> 0.4.1-13
- Third try is the charm
- Resolves: #1092515

* Tue Sep 06 2016 Robbie Harwood <rharwood@redhat.com> 0.4.1-12
- Restore _FORTIFY_SOURCE behavior
- Resolves: #1092515

* Tue Sep 06 2016 Robbie Harwood <rharwood@redhat.com> 0.4.1-11
- Actually harden build with PIE and RELRO
- Resolves: #1092515

* Fri Jun 10 2016 Robbie Harwood <rharwood@redhat.com> 0.4.1-10
- Fix behavior with multiple keys in a keytab
- Resolves: #1285012

* Tue Jun 07 2016 Robbie Harwood <rharwood@redhat.com> 0.4.1-9
- Re-open socket in mechglue if client forks/changes privilege
- Resolves: #1340259

* Wed Mar 30 2016 Robbie Harwood <rharwood@redhat.com> 0.4.1-8
- Make GSS-Proxy work with krb5-1.14
- resolves: #1292487

* Tue Sep 29 2015 Simo Sorce <simo@redhat.com> 0.4.1-7
- Fix loop cause by imporper EINTR handling
- resolves: #1266564

* Mon Aug 24 2015 Roland Mainz <rmainz@redhat.com> 0.4.1-6
- Remove extra whitespaces from #1208640/#1194299 patches
- spec file cleanup
related: #1208640 #1194299

* Wed Aug 19 2015 Robbie Harwood <rharwood@redhat.com> 0.4.1-5
- Carry service/HTTP default conf section
- resolves: #1208640

* Wed Aug 19 2015 Robbie Harwood <rharwood@redhat.com> 0.4.1-4
- Set default rcache location patch
- resolves: #1194299

* Mon Jul 13 2015 Roland Mainz <rmainz@redhat.com> 0.4.1-3
- Bug #1213852 ("[gssproxy] NFS clients cannot mount with
  sec=krb5 if the NFS server is running gssproxy") was
  fixed by the rebase to 0.4.1 in bug ("[RFE] Rebase
  gssproxy to the latest to match expectations of other
  projects").
  Note that the same bug was also fixed in the kernel with
  "9507271 svcrpc: fix potential GSSX_ACCEPT_SEC_CONTEXT
  decoding failures" (see
  https://bugzilla.redhat.com/show_bug.cgi?id=1213852#c2
  and RH Bug #1120860 ("[NFS] NFS clients cannot mount with
  sec=krb5 if the NFS server is running gssproxy")) to
  handle various corner cases not covered by gssproxy,
  for example individual krb5 ticket fields exceeding
  the kernel's buffer size.

* Thu Jul 9 2015 Roland Mainz <rmainz@redhat.com> 0.4.1-2
- The following bugs have been fixed by the rebase to 0.4.1
  in bug ("[RFE] Rebase gssproxy to the latest to match
  expectations of other projects"):
  - Bug #1196371 ("rpc.gssd segfaults in gssproxy (proxymech.so)")
    Upstream tickets { #137, #144 }
  - Bug #1053730 ("KrbLocalUserMapping does not work with
    Apache & GSS-Proxy")
    Upstream ticket #101
  - Bug #1168962 ("gssproxy is not working with httpd on ppc64 and s390x")
    Upstream ticket #146

* Thu Jul 9 2015 Roland Mainz <rmainz@redhat.com> 0.4.1-1
- Add patch to remove -fno-strict-aliasing (gssproxy ticket #140,
  a dependicy for the fix for bug #1092515 (see below))
- Add patch to fix bug #1092515 ("gssproxy - PIE and RELRO check")

* Fri Jun 5 2015 Roland Mainz <rmainz@redhat.com> 0.4.1-0
- Rebase gssproxy to 0.4.1 per bug #1132389 ("[RFE] Rebase
  gssproxy to the latest to match expectations of other
  projects").

* Fri Jan 23 2015 Simo Sorce <ssorce@redhat.com> 0.3.0-10
- Fix crash bug affecting updated rpc.gssd
- resolves: #1184531

* Wed Mar 12 2014 Guenther Deschner <gdeschner@redhat.com> 0.3.0-9
- Fix potential mutex deadlock
- resolves: #1075268

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.3.0-8
- Mass rebuild 2014-01-24

* Thu Jan 16 2014 Guenther Deschner <gdeschner@redhat.com> 0.3.0-7
- Fix nfsd startup
- resolves: https://fedorahosted.org/gss-proxy/ticket/114
- resolves: #1053710

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.3.0-6
- Mass rebuild 2013-12-27

* Tue Dec 17 2013 Guenther Deschner <gdeschner@redhat.com> 0.3.0-5
- Fix flags handling.
- resolves: https://fedorahosted.org/gss-proxy/ticket/112
- related: #1031710

* Wed Nov 27 2013 Guenther Deschner <gdeschner@redhat.com> 0.3.0-4
- Use secure_getenv
- resolves: https://fedorahosted.org/gss-proxy/ticket/110
- resolves: #1032684
- Use strerror_r instead of strerror
- resolves: https://fedorahosted.org/gss-proxy/ticket/111
- resolves: #1033350

* Tue Nov 19 2013 Guenther Deschner <gdeschner@redhat.com> 0.3.0-3
- Fix flags handling in gss_init_sec_context()
- resolves: https://fedorahosted.org/gss-proxy/ticket/106
- resolves: #1031713
- Fix OID handling in gss_inquire_cred_by_mech()
- resolves: https://fedorahosted.org/gss-proxy/ticket/107
- resolves: #1031712
- Fix continuation processing for not yet fully established contexts.
- resolves: https://fedorahosted.org/gss-proxy/ticket/108
- resolves: #1031711
- Add flags filtering and flags enforcing.
- resolves: https://fedorahosted.org/gss-proxy/ticket/109
- resolves: #1031710

* Wed Oct 23 2013 Guenther Deschner <gdeschner@redhat.com> 0.3.0-0
- New upstream release 0.3.0:
  * Add support for impersonation (depends on s4u2self/s4u2proxy on the KDC)
  * Add support for new rpc.gssd mode of operation that forks and changes uid
  * Add 2 new options allow_any_uid and cred_usage

* Fri Oct 18 2013 Guenther Deschner <gdeschner@redhat.com> 0.2.3-8
- Fix default proxymech documentation and fix LOCAL_FIRST implementation
- resolves: https://fedorahosted.org/gss-proxy/ticket/105

* Wed Jul 24 2013 Guenther Deschner <gdeschner@redhat.com> 0.2.3-6
- Add better default gssproxy.conf file for nfs client and server usage

* Thu Jun 06 2013 Guenther Deschner <gdeschner@redhat.com> 0.2.3-5
- New upstream release

* Fri May 31 2013 Guenther Deschner <gdeschner@redhat.com> 0.2.2-5
- Require libverto-tevent to make sure libverto initialization succeeds

* Wed May 29 2013 Guenther Deschner <gdeschner@redhat.com> 0.2.2-4
- Modify systemd unit files for nfs-secure services

* Wed May 22 2013 Guenther Deschner <gdeschner@redhat.com> 0.2.2-3
- Fix cred_store handling w/o client keytab

* Thu May 16 2013 Guenther Deschner <gdeschner@redhat.com> 0.2.2-2
- New upstream release

* Tue May 07 2013 Guenther Deschner <gdeschner@redhat.com> 0.2.1-2
- New upstream release

* Wed Apr 24 2013 Guenther Deschner <gdeschner@redhat.com> 0.2.0-1
- New upstream release

* Mon Apr 01 2013 Simo Sorce <simo@redhat.com> - 0.1.0-0
- New upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 06 2012 Guenther Deschner <gdeschner@redhat.com> 0.0.3-7
- Update to 0.0.3

* Wed Aug 22 2012 Guenther Deschner <gdeschner@redhat.com> 0.0.2-6
- Use new systemd-rpm macros
- resolves: #850139

* Wed Jul 18 2012 Guenther Deschner <gdeschner@redhat.com> 0.0.2-5
- More spec file fixes

* Mon Jul 16 2012 Guenther Deschner <gdeschner@redhat.com> 0.0.2-4
- Fix systemd service file

* Fri Jul 13 2012 Guenther Deschner <gdeschner@redhat.com> 0.0.2-3
- Fix various packaging issues

* Mon Jul 02 2012 Guenther Deschner <gdeschner@redhat.com> 0.0.1-2
- Add systemd packaging

* Wed Mar 28 2012 Guenther Deschner <gdeschner@redhat.com> 0.0.1-1
- Various fixes

* Mon Dec 12 2011 Simo Sorce <simo@redhat.com> - 0.0.2-0
- Automated build of the gssproxy daemon
