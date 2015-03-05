%global		redhatssgversion	19

Name:		scap-security-guide
Version:	0.1.%{redhatssgversion}
Release:	2%{?dist}
Summary:	Security guidance and baselines in SCAP formats

Group:		System Environment/Base
License:	Public Domain
URL:		https://fedorahosted.org/scap-security-guide/

Source0:	http://repos.ssgproject.org/sources/%{name}-%{version}.tar.gz
Patch1:		scap-security-guide-0.1.19-rhel7-include-only-rht-ccp-profile.patch
Patch2:		scap-security-guide-0.1.19-rhel7-drop-restorecond-since-in-optional.patch
Patch3:		scap-security-guide-0.1.19-rhel7-drop-cpuspeed-rule-since-obsolete.patch
Patch4:		scap-security-guide-0.1.19-update-man-page-for-rhel7-content.patch
Patch5:		scap-security-guide-0.1.19-rhel7-update-pam-XCCDF-to-use-pam_pwquality.patch
Patch6:		scap-security-guide-0.1.20-rhel7-shared-fix-limit-password-reuse-remediation.patch
Patch7:		scap-security-guide-0.1.20-rhel6-rhel7-PR#280-set-deny-prerequisite-#1.patch
Patch8:		scap-security-guide-0.1.20-rhel6-rhel7-set-deny-prerequisite-#2.patch
Patch9:		scap-security-guide-0.1.20-shared-fix-set-deny-for-failed-password-attempts-remediation.patch
Patch10:	scap-security-guide-0.1.20-rhel7-specify-exact-profile-name-when-generating-guide.patch
BuildArch:	noarch

BuildRequires:	libxslt, expat, python, openscap-scanner >= 1.1.1, python-lxml
Requires:	xml-common, openscap-scanner >= 1.1.1

%description
The scap-security-guide project provides a guide for configuration of the
system from the final system's security point of view. The guidance is
specified in the Security Content Automation Protocol (SCAP) format and
constitutes a catalog of practical hardening advice, linked to government
requirements where applicable. The project bridges the gap between generalized
policy requirements and specific implementation guidelines. The Red Hat
Enterprise Linux 7 system administrator can use the oscap command-line tool
from the openscap-utils package to verify that the system conforms to provided
guideline. Refer to scap-security-guide(8) manual page for further information.

%prep
%setup -q -n %{name}-%{version}
# For RHEL-7 include only RHT-CCP profile
%patch1 -p1 -b .rht-ccp-only
# Drop restorecond due to https://github.com/OpenSCAP/scap-security-guide/issues/258
%patch2 -p1 -E -b .drop-restorecond
# Drop cpuspeed rule since obsoleted in Fedora-16 by cpupower from kernel-tools RPM
# http://marc.info/?l=fedora-devel-list&m=131107769617369&w=2
%patch3 -p1 -b .drop-cpuspeed
# Update manual page to be more appropriate against RHEL-7
%patch4 -p1 -b .manual-page
# Update pam.xml to use pam_pwquality instead of pam_cracklib
%patch5 -p1 -b .replace-pam_cracklib
# Fix 'Limit Password Reuse' remediation error
%patch6 -p1 -b .reuse
# Fix 'Set Deny For Failed Password Attempts' remediation error
%patch7 -p1
%patch8 -p1
%patch9 -p1 -b .set-deny
# Specify exact profile name when generating RHEL-7 HTML guide
%patch10 -p1 -b .exact-profile

%build
(cd RHEL/6 && make dist)
(cd RHEL/7 && make dist)

%install

mkdir -p %{buildroot}%{_datadir}/xml/scap/ssg/content
mkdir -p %{buildroot}%{_mandir}/en/man8/

# Add in RHEL-7 core content (SCAP)
cp -a RHEL/7/dist/content/* %{buildroot}%{_datadir}/xml/scap/ssg/content/

# Add in RHEL-6 datastream (SCAP)
cp -a RHEL/6/dist/content/ssg-rhel6-ds.xml %{buildroot}%{_datadir}/xml/scap/ssg/content

# Add in manpage
cp -a RHEL/6/input/auxiliary/scap-security-guide.8 %{buildroot}%{_mandir}/en/man8/scap-security-guide.8

%files
%defattr(-,root,root,-)
%{_datadir}/xml/scap
%lang(en) %{_mandir}/en/man8/scap-security-guide.8.gz
%doc RHEL/6/LICENSE RHEL/6/output/rhel6-guide.html RHEL/7/output/rhel7-ccp-guide.html RHEL/6/output/table-rhel6-cces.html RHEL/7/output/table-rhel7-cces.html RHEL/6/output/table-rhel6-nistrefs-common.html RHEL/6/output/table-rhel6-nistrefs.html RHEL/6/output/table-rhel6-srgmap-flat.html RHEL/6/output/table-rhel6-srgmap-flat.xhtml RHEL/6/output/table-rhel6-srgmap.html RHEL/6/output/table-rhel6-stig.html RHEL/6/input/auxiliary/DISCLAIMER

%changelog
* Tue Oct 21 2014 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.19-2
- Fix Limit Password Reuse remediation script error
- Fix Set Deny For Failed Password Attempts remediation script error
- Use RHT-CCP profile name when generating HTML guide
- Describe RHT-CCP profile in the manual page

* Mon Sep 29 2014 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.19-1
- Include RHEL-7 content (RHT-CCP profile only)
- Drop RHEL-7 restorecond XCCDF rule since policycoreutils-restorecond in Optional channel
- Drop RHEL-7 cpuspeed XCCDF rule since obsoleted by cpupower from kernel-tools
- Update manual page to be more appropriate for RHEL-7
- Drop RHEL-6 C2S profile update patch since merged upstream

* Tue Sep 02 2014 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.18-4
- Initial build for Red Hat Enterprise Linux 7

* Thu Aug 28 2014 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.18-3
- Update C2S profile <description> per request from CIS

* Thu Jun 26 2014 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.18-2
- Include the upstream STIG for RHEL 6 Server profile disclaimer file too

* Sun Jun 22 2014 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.18-1
- Make new 0.1.18 release

* Wed May 14 2014 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.17-2
- Drop vendor line from the spec file. Let the build system to provide it.

* Fri May 09 2014 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.17-1
- Upgrade to upstream 0.1.17 version

* Mon May 05 2014 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.16-2
- Initial RPM for RHEL base channels

* Mon May 05 2014 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.16-1
- Change naming scheme (0.1-16 => 0.1.16-1)

* Fri Feb 21 2014 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1-16
- Include datastream file into RHEL6 RPM package too
- Bump version

* Tue Dec 24 2013 Shawn Wells <shawn@redhat.com> 0.1-16.rc2
+ RHEL6 stig-rhel6-server XCCDF profile renamed to stig-rhel6-server-upstream

* Mon Dec 23 2013 Shawn Wells <shawn@redhat.com> 0.1-16.rc1
- [bugfix] RHEL6 no_empty_passwords remediation script overwrote
  system-auth symlink. Added --follow-symlink to sed command.

* Fri Nov 01 2013 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1-15
- Version bump

* Sat Oct 26 2013 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1-15.rc5
- Point the spec's source to proper remote tarball location
- Modify the main Makefile to use remote tarball when building RHEL/6's SRPM

* Sat Oct 26 2013 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1-15.rc4
- Don't include the table html files two times
- Remove makewhatis

* Fri Oct 25 2013 Shawn Wells <shawn@redhat.com> 0.1-15.rc3
- [bugfix] Updated rsyslog_remote_loghost to scan /etc/rsyslog.conf and /etc/rsyslog.d/*
- Numberous XCCDF->OVAL naming schema updates
- All rules now have CCE

* Fri Oct 25 2013 Shawn Wells <shawn@redhat.com> 0.1-15.rc2
- RHEL/6 HTML table naming bugfixes (table-rhel6-*, not table-*-rhel6)

* Fri Oct 25 2013 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1-15.rc1
- Apply spec file changes required by review request (RH BZ#1018905)

* Thu Oct 24 2013 Shawn Wells <shawn@redhat.com> 0.1-14
- Formal RPM release
- Inclusion of rht-ccp profile
- OVAL unit testing patches
- Bash remediation patches
- Bugfixes

* Mon Oct 07 2013 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1-14.rc1
- Change RPM versioning scheme to include release into tarball

* Sat Sep 28 2013 Shawn Wells <shawn@redhat.com> 0.1-13
- Updated RPM spec file to fix rpmlint warnings

* Wed Jun 26 2013 Shawn Wells <shawn@redhat.com> 0.1-12
- Updated RPM version to 0.1-12

* Fri Apr 26 2013 Shawn Wells <shawn@redhat.com> 0.1-11
- Significant amount of OVAL bugfixes
- Incorporation of Draft RHEL/6 STIG feedback

* Sat Feb 16 2013 Shawn Wells <shawn@redhat.com> 0.1-10
- `man scap-security-guide`
- OVAL bug fixes
- NIST 800-53 mappings update

* Wed Nov 28 2012 Shawn Wells <shawn@redhat.com> 0.1-9
- Updated BuildRequires to reflect python-lxml (thank you, Ray S.!)
- Reverting to noarch RPM

* Tue Nov 27 2012 Shawn Wells <shawn@redhat.com> 0.1-8
- Significant copy editing to XCCDF rules per community
  feedback on the DISA RHEL/6 STIG Initial Draft

* Thu Nov 1 2012 Shawn Wells <shawn@redhat.com> 0.1-7
- Corrected XCCDF content errors
- OpenSCAP now supports CPE dictionaries, important to
  utilize --cpe-dict when scanning machines with OpenSCAP,
  e.g.:
  $ oscap xccdf eval --profile stig-server \
   --cpe-dict ssg-rhel6-cpe-dictionary.xml ssg-rhel6-xccdf.xml

* Mon Oct 22 2012 Shawn Wells <shawn@redhat.com> 0.1-6
- Corrected RPM versioning, we're on 0.1 release 6 (not version 1 release 6)
- Updated RPM includes feedback received from DoD Consensus meetings

* Fri Oct 5  2012 Jeffrey Blank <blank@eclipse.ncsc.mil> 1.0-5
- Adjusted installation directory to /usr/share/xml/scap.

* Tue Aug 28  2012 Spencer Shimko <sshimko@tresys.com> 1.0-4
- Fix BuildRequires and Requires.

* Tue Jul 3 2012 Jeffrey Blank <blank@eclipse.ncsc.mil> 1.0-3
- Modified install section, made description more concise.

* Thu Apr 19 2012 Spencer Shimko <sshimko@tresys.com> 1.0-2
- Minor updates to pass some variables in from build system.

* Mon Apr 02 2012 Shawn Wells <shawn@redhat.com> 1.0-1
- First attempt at SSG RPM. May ${deity} help us...
