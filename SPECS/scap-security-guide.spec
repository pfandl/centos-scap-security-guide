%global		redhatssgversion	40

# Somehow, _pkgdocdir is already defined and points to unversioned docs dir
# RHEL 7.X uses versioned docs dir, hence the definition below
%global _pkgdocdir %{_docdir}/%{name}-%{version}

Name:		scap-security-guide
Version:	0.1.%{redhatssgversion}
Release:	13%{?dist}
Summary:	Security guidance and baselines in SCAP formats

Group:		System Environment/Base
License:	BSD-3-Clause
URL:		https://github.com/OpenSCAP/scap-security-guide
Source0:	%{name}-%{version}.tar.bz2
Patch1: 	scap-security-guide-0.1.33-update-upstream-manual-page.patch
Patch2: 	scap-security-guide-0.1.41-restrict-remediation-for-dev-shm.patch
Patch3: 	scap-security-guide-0.1.41-drop-dev-cdrom-fix.patch
Patch4: 	scap-security-guide-0.1.41-install-dracut-fips.patch
Patch5: 	scap-security-guide-0.1.41-audit_unset_4294967295.patch
Patch6: 	scap-security-guide-0.1.41-audit_file_deletion.patch
Patch7: 	scap-security-guide-0.1.41-audit_misc_improvements.patch
Patch8: 	scap-security-guide-0.1.41-audit_file_ownership.patch
Patch9: 	scap-security-guide-0.1.41-audit_file_permission.patch
Patch10: 	scap-security-guide-0.1.41-audit_log_access.patch
Patch11: 	scap-security-guide-0.1.41-audit_privileged_commands.patch
Patch12: 	scap-security-guide-0.1.41-audit_file_open.patch
Patch13: 	scap-security-guide-0.1.41-audit_file_open_ospp.patch
Patch14:        scap-security-guide-0.1.41-audit_passwd_log_writes.patch
Patch15: 	scap-security-guide-0.1.41-ospp_enable.patch
Patch16:        scap-security-guide-0.1.41-template_syscall_rules.patch
Patch17:        scap-security-guide-0.1.41-template_syscall_rules_ospp.patch
Patch18:        scap-security-guide-0.1.41-template_watch_path.patch
Patch19:        scap-security-guide-0.1.41-template_watch_path_build_templates.patch
Patch20:        scap-security-guide-0.1.41-fix_audit_rules_unsuccessful_file_modification_regex.patch
Patch21:	scap-security-guide-0.1.41-fix_unauthorized_syscall_regex.patch
Patch22:        scap-security-guide-0.1.41-fix_syscall_in_last_position.patch
Patch23:        scap-security-guide-0.1.41-fix_dconf_gnome_screensaver_lock_enabled.patch
Patch24:        scap-security-guide-0.1.41-untemplate_var_tmp.patch
Patch25:		scap-security-guide-0.1.41-bash_and_tests_for_grub2_audit_argument.patch
Patch26:		scap-security-guide-0.1.41-small_bash_fix_for_gnome_screensaver_lock_delay.patch
Patch27:		scap-security-guide-0.1.41-select_missing_arpc_for_OSPP42.patch
Patch28:		scap-security-guide-0.1.41-fix_owners_groups.patch
Patch29:		scap-security-guide-0.1.41-packages_abrt_sendmail_removed.patch
Patch30:		scap-security-guide-0.1.41-dev_shm_mount_option.patch
Patch31:		scap-security-guide-0.1.41-sysctl_kernel.patch
Patch32:		scap-security-guide-0.1.41-kptr_restrict.patch
Patch33:		scap-security-guide-0.1.41-grub2_bootloader_arguments.patch
Patch34:		scap-security-guide-0.1.41-profile_title_rename_etc.patch
Patch35:		scap-security-guide-0.1.42-rule_yml_platform_tag_support.patch
Patch36:		scap-security-guide-0.1.42-mark_rules_as_machine_only.patch
Patch37:		scap-security-guide-0.1.45-mark_rules_as_machine_only_v2.patch
Patch38:		scap-security-guide-0.1.44-cpe-shadow-utils.patch
Patch39:		scap-security-guide-0.1.44-cpe-pam-systemd-yum.patch
Patch40:		scap-security-guide-0.1.44-cpe-gdm.patch
Patch41:		scap-security-guide-0.1.44-cpe-remaining.patch
Patch42:		scap-security-guide-0.1.44-update-cpe-dictionary.patch
Patch999:               centos-debranding.patch

BuildArch:	noarch

BuildRequires:	libxslt, expat, python, openscap-scanner >= 1.2.16, python-jinja2, cmake >= 2.8, PyYAML
Requires:	xml-common, openscap-scanner >= 1.2.5

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

%package	doc
Summary:	HTML formatted documents containing security guides generated from XCCDF benchmarks.
Group:		System Environment/Base
Requires:	%{name} = %{version}-%{release}

%description	doc
The %{name}-doc package contains HTML formatted documents containing security guides that have
been generated from XCCDF benchmarks present in %{name} package.

%prep
%setup -q -n %{name}-%{version}
mkdir build
# Update manual page to drop the part dedicated to Fedora content
%patch1 -p1 -b .man_page_update
%patch2 -p1 -b .remediation_for_dev_shm
%patch3 -p1 -b .remediation_for_dev_cdrom
%patch4 -p1 -b .install_dracut_fips
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch999 -p1

%build
mkdir -p build && cd build
%cmake -D CMAKE_INSTALL_DOCDIR=%{_pkgdocdir} \
-DSSG_PRODUCT_CHROMIUM:BOOL=OFF \
-DSSG_PRODUCT_DEBIAN8:BOOL=OFF \
-DSSG_PRODUCT_FEDORA:BOOL=OFF \
-DSSG_PRODUCT_JBOSS_EAP6:BOOL=OFF \
-DSSG_PRODUCT_JBOSS_FUSE6:BOOL=OFF \
-DSSG_PRODUCT_OCP3:BOOL=OFF \
-DSSG_PRODUCT_OPENSUSE:BOOL=OFF \
-DSSG_PRODUCT_OSP7:BOOL=OFF \
-DSSG_PRODUCT_SUSE11:BOOL=OFF \
-DSSG_PRODUCT_SUSE12:BOOL=OFF \
-DSSG_PRODUCT_UBUNTU14:BOOL=OFF \
-DSSG_PRODUCT_UBUNTU16:BOOL=OFF \
-DSSG_PRODUCT_WRLINUX:BOOL=OFF \
-DSSG_PRODUCT_OL7:BOOL=OFF \
-DSSG_CENTOS_DERIVATIVES_ENABLED:BOOL=ON \
-DSSG_SCIENTIFIC_LINUX_DERIVATIVES_ENABLED:BOOL=OFF \
../
make %{?_smp_mflags}

%check
cd build
ctest %{?_smp_mflags} -E linkchecker --output-on-failure

%install
cd build
%make_install

%files
%defattr(-,root,root,-)
%{_datadir}/xml/scap
%{_datadir}/%{name}
%lang(en) %{_mandir}/man8/scap-security-guide.8.gz
%doc LICENSE
%doc Contributors.md
%doc README.md
%doc DISCLAIMER
# All files installed by cmake are automatically include in main package
# We exclude the guides to here add them in doc package
%exclude %{_pkgdocdir}/guides/

%files doc
%defattr(-,root,root,-)
%doc build/guides/ssg-*-guide-*.html

%changelog
* Tue Apr 23 2019 Johnny Hughes <johnny@centos.org>
- Manual CentOS Debranding

* Thu Apr 11 2019 Gabriel Becker <ggasparb@redhat.com> - 0.1.40-13
- Added support to platform tag and mark rules as machine only (RHBZ#1698752)
- Fix content support for UBI-Minimal (RHBZ#1698751)

* Tue Sep 25 2018 Watson Yuuma Sato <wsato@redhat.com> - 0.1.40-12
- Fix malformed patch for removal of abrt and sendmail (RHBZ#1619689)

* Tue Sep 25 2018 Matěj Týč <matyc@redhat.com> - 0.1.40-11
- Fixes for RHBZ#1619689:
- Added support for kernel parameters yama.ptrace_scope, kptr_restrict, dmesg_restrict and kexec_load_disabled.
- Added support for boot parameters audit_backlog_limit=8192, slub_debug=P, page_poison=1 and vsyscall=none.
- Added support for proper /dev/shm handling (noexec,nosuid,nodev,mode=1777)
- Added support for checking that sendmail and abrt are not installed.
- Introduced OSPP to the OSPP profile title.
- Disabled linkcheck tests during the build.

* Sun Sep 23 2018 Marek Haičman <mhaicman@redhat.com> - 0.1.40-10
- Fix regression in file ownership and group OVAL. (RHBZ#1570802)

* Fri Sep 21 2018 Watson Yuuma Sato <wsato@redhat.com> - 0.1.40-9
- Fix malformed patch for Audit Rules (RHBZ#1619689)

* Fri Sep 21 2018 Watson Yuuma Sato <wsato@redhat.com> - 0.1.40-8
- Add Bash remediation for rule grub2_audit_arguments (RHBZ#1619689)
- Allow remediation for rule dconf_gnome_screensaver_lock_delay to fix commented settings (RHBZ#1609122)
- Select missing audit rules for privileged commands for OSPP4.2 Profile (RHBZ#1619689)

* Wed Sep 19 2018 Matěj Týč <matyc@redhat.com> - 0.1.40-7
- Fixed previously applied patches for OSPP 4.2 (RHBZ#1619689)

* Mon Sep 17 2018 Matěj Týč <matyc@redhat.com> - 0.1.40-6
- Applied a batch of patches that improve OSPP 4.2 profile support for RHEL7 (RHBZ#1619689)
- Fixed the xccdf_org.ssgproject.content_rule_dconf_gnome_screensaver_lock_enabled check (RHBZ#1609122)

* Fri Sep 14 2018 Marek Haičman <mhaicman@redhat.com> - 0.1.40-5
- Re-fix FIPS patch. (RHBZ#1587911)

* Wed Sep 12 2018 Matěj Týč <matyc@redhat.com> - 0.1.40-4
- Applied a batch of patches that improve OSPP 4.2 profile support for RHEL7 (RHBZ#1619689)

* Tue Sep 11 2018 Matěj Týč <matyc@redhat.com> - 0.1.40-3
- Don't generate remediations for Anaconda for /dev/cdrom mount point (RHBZ#1618840)
- Install dracut-fips when fips mode is enabled in the profile (RHBZ#1587911)

* Wed Aug 01 2018 Watson Yuuma Sato <wsato@redhat.com> - 0.1.40-2
- Don't generate remediations for Anaconda for /dev/shm mount point (RHBZ#1570956)

* Wed Jul 25 2018 Matěj Týč <matyc@redhat.com> - 0.1.40-1
- Update to upstream release 0.1.40
- Underlying code has been deduplicated and unified, which fixes countless subtle bugs.
- Updated Ansible playbooks, so they don't use deprecated constructs.
- Service disable family of rules take the corresponding socket deactivation into account if applicable in check and in remediations.

* Thu Jul 19 2018 Watson Yuuma Sato <wsato@redhat.com> - 0.1.39-2
- Fix configuration to not build new products introduced in upstream
- Test package with ctest

* Fri Jul 13 2018 Watson Yuuma Sato <wsato@redhat.com> - 0.1.39-1
- Update to upstream release 0.1.39
- Profile IDs simplified
- Common Profile removed in favor of Standard Profile
- RHEL7 STIG reference updated to V1R4
- RHEL6 STIG reference updated to V1R18
- New License - BSD-3 Clause
- Several remediation fixes
- Better content support for DISA STIG Viewer (#2418)

* Mon Jan 08 2018 Watson Yuuma Sato <wsato@redhat.com> - 0.1.36-7
- Fix sshd_required unset (RHBZ#1522956)
- Fix missing bash remediation functions include (RHBZ#1524738)
- Fix empty columns in SRG HTML Table (RHBZ#1531105)
- Fix reference to oudated PAM config manual (RHBZ#1447760)

* Tue Dec 12 2017 Watson Yuuma Sato <wsato@redhat.com> - 0.1.36-6
- Rebuild with OpenSCAP 1.2.16

* Mon Dec 11 2017 Matěj Týč <matyc@redhat.com> - 0.1.36-5
- Patched not to check library ownership in libexec.
- Patched to fix title of DISA STIG profile.
- Patched to deprecate RhostsRSAAuthentication.
- Patched to fix umask_for_daemons.

* Thu Nov 16 2017 Watson Yuuma Sato <wsato@redhat.com> - 0.1.36-4
- Rebuild with OpenSCAP 1.2.16

* Tue Nov 14 2017 Watson Yuuma Sato <wsato@redhat.com> - 0.1.36-3
- Add DISA STIG Rule IDs to XCCDF Rules with STIGID

* Fri Nov 03 2017 Watson Yuuma Sato <wsato@redhat.com> - 0.1.36-2
- Fix configuration to not build new products introduced in upstream

* Fri Nov 03 2017 Watson Yuuma Sato <wsato@redhat.com> - 0.1.36-1
- Update to upstream release 0.1.36
- Introduction of SCAP Security Guide Test Suite
- Better alignment of RHEL6 and RHEL7 with DISA STIG
- Remove JBoss EAP5 content due to being End-of-Life
- New STIG Profile for JBOSS EAP 6
- Updates in C2S Profile for RHEL 7
- Variables can be directly tailored in Ansible roles
- Content presents less false positives in containers
- Changes in directory layout

* Wed Sep 20 2017 Watson Yuuma Sato <wsato@redhat.com> - 0.1.35-2
- Do not build content for JBOSS EAP6

* Wed Sep 20 2017 Watson Yuuma Sato <wsato@redhat.com> - 0.1.35-1
- Update to upstream release 0.1.35
- Remove Red Hat Enterprise Linux 5 content due to being End-of-Life March 31, 2017
- Added several templates for OVAL checks
- Many optimizations in build process
- Different title for PCI-DSS Benchmark variants
- Remediation roles moved to /usr/share/scap-security
- Fix duplicated roles and guides (RHBZ#1465691)

* Tue Sep 19 2017 Watson Sato <wsato@redhat.com> 0.1.33-6
- Dropped remediation that makes system not accessible by SSH (RHBZ#1478414)

* Wed Jun 14 2017 Watson Sato <wsato@redhat.com> 0.1.33-5
- Fix Anaconda Smartcard auth remediation (RHBZ#1461330)

* Fri May 19 2017 Watson Sato <wsato@redhat.com> 0.1.33-4
- Fix specfile to not include tables twice

* Fri May 19 2017 Watson Sato <wsato@redhat.com> 0.1.33-3
- Fix malformed title of profile nist-800-171-cui

* Fri May 19 2017 Watson Sato <wsato@redhat.com> 0.1.33-2
- Fix emtpy ospp-rhel7 table
- Fix Anaconda remediation templates (RHBZ#1450731)

* Mon May 01 2017 Watson Sato <wsato@redhat.com> 0.1.33-1
- Update to upstream version 0.1.33
- DISA RHEL7 STIG profile alignment improved
- Introduction of remediation roles
- RPM and DEB test packages are built by CMake with CPack
- Lots of remediation fixes

* Tue Mar 28 2017 Watson Sato <wsato@redhat.com> 0.1.32-1
- Update to upstream version 0.1.32
- New CMake build system
- Improved NIST 800-171 profile
- Initial RHVH profile
- New CPE to identify systems like machines (bare-metal and VM) and containers (image and container)
- Template clean up in lots of remediations

* Fri Mar 10 2017 Watson Sato <wsato@redhat.com> 0.1.30-6
- Ship separate OCIL definitions for Red Hat Enterprise Linux 7 (RHBZ#1428144)

* Tue Feb 14 2017 Watson Sato <wsato@redhat.com> 0.1.30-5
- Fix template remediation function used by SSHD remediation
- Reduce scope of patch that fixes SSHD remediation (RH BZ#1415152)

* Tue Jan 31 2017 Watson Sato <wsato@redhat.com> 0.1.30-4
- Correct remediation for SSHD which caused it not to start (RH BZ#1415152)

* Wed Aug 10 2016 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.30-3
- Correct the remediation script for 'Enable Smart Card Login' rule
  for Red Hat Enterprise Linux 7 (RH BZ#1357019)

* Thu Jul 14 2016 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.30-2
- Fix issue of two STIG profiles for Red Hat Enterprise Linux 6 benchmark
  having the identical title (RH BZ#1351541)
- Enhance the shared OVAL check for 'Set Deny For Failed Password Attempts'
  rule and also Red Hat Enterprise Linux 7 OVAL check for 'Configure the root
  Account for Failed Password Attempts' rule to report correct system status
  WRT to these requirements also in the case the SSSD daemon is used
  (RH BZ#1344581)
- Include currently available kickstart files and produced HTML tables for
  Red Hat Enterprise Linux 6 and 7 products into the produced RPM package
  (RH BZ#1351751)

* Wed Jun 22 2016 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.30-1
- Update to upstream's 0.1.30 release:
  https://github.com/OpenSCAP/scap-security-guide/releases/tag/v0.1.30
  (RH BZ#1289533)
- Drop remediation functions library since starting from 0.1.30 release
  remediation scripts are part of the benchmarks directly
- Drop three patches that have been accepted upstream in the meantime
- Update drop-rpm-verify-permissions-rule patch to work properly against
  0.1.30 release

* Fri Oct 02 2015 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.25-3
- Drop "Verify and Correct File Permissions with RPM" rule from the PCI-DSS
  profile for Red Hat Enterprise Linux 7 (RH BZ#1267861)

* Wed Sep 09 2015 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.25-2
- Update R and BR for the openscap-scanner package to 1.2.5 per RHBZ#1202762#c7

* Wed Aug 19 2015 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.25-1
- Rebase to upstream 0.1.25 release

* Tue Aug 04 2015 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.24-4
- Fix false-positive in OVAL check for 'accounts_passwords_pam_faillock_deny'
  rule

* Mon Aug 03 2015 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.24-3
- Add remediation script for 'accounts_passwords_pam_faillock_unlock_time' rule
  for Red Hat Enterprise Linux 7 product
- Override title and description for all existing profiles for Red Hat
  Enterprise Linux 6 product that are extending another SCAP profile
  (RHBZ#1246529)
- Correct various issues in the included Oscap Anaconda Addon PCI-DSS profile
  kickstart file for Red Hat Enterprise Linux 7 product
- Add remediation script for 'audit_rules_time_clock_settime' rule for
  Red Hat Enterprise Linux 7 product
- Add remediation scripts for 'audit_rules_time_adjtimex',
  'audit_rules_time_settimeofday', and 'audit_rules_time_stime' rules for
  Red Hat Enterprise Linux 7 product
- Tag current PCI-DSS profile for Red Hat Enterprise Linux 7 product with
  "Draft" label
- Disable the following rules in the PCI-DSS profile for the Red Hat Enterprise
  Linux 7 product:
  * dconf_gnome_screensaver_idle_delay -- missing remediation script,
  * dconf_gnome_screensaver_idle_activation -- missing remediation script,
  * dconf_gnome_screensaver_lock_enabled -- missing remediation script,
  * audit_rules_login_events -- incorrect OVAL check (upstream issue #607),
  * audit_rules_privileged_commands -- missing remediation script, and
  * audit_rules_immutable -- missing remediation script.

* Mon Aug 03 2015 Martin Preisler <mpreisle@redhat.com> 0.1.24-2
- Break-down firewalld rule description for Red Hat Enterprise Linux 7 product
  into multiple lines, prevents HTML guide UX issues

* Tue Jul 07 2015 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.24-1
- Rebase to upstream scap-security-guide-0.1.24 version
- Start producing the -doc subpackage to provide the HTML formatted
  documents containing security guides generated from shipped XCCDF benchmarks

* Mon Jun 22 2015 Jan iankko Lieskovsky <jlieskov@redhat.com> 0.1.23-1
- Rebase to upstream scap-security-guide-0.1.23 version
- Update upstream tarball source URL to GitHub archive location
- Drop the following patches that have been accepted upstream:
  * scap-security-guide-0.1.19-rhel7-include-only-rht-ccp-profile.patch
  * scap-security-guide-0.1.19-rhel7-drop-restorecond-since-in-optional.patch
  * scap-security-guide-0.1.19-update-man-page-for-rhel7-content.patch
  * scap-security-guide-0.1.19-rhel7-update-pam-XCCDF-to-use-pam_pwquality.patch
  * scap-security-guide-0.1.20-rhel7-shared-fix-limit-password-reuse-remediation.patch
  * scap-security-guide-0.1.20-rhel6-rhel7-PR#280-set-deny-prerequisite-#1.patch
  * scap-security-guide-0.1.20-rhel6-rhel7-set-deny-prerequisite-#2.patch
  * scap-security-guide-0.1.20-shared-fix-set-deny-for-failed-password-attempts-remediation.patch
  * scap-security-guide-0.1.20-rhel7-specify-exact-profile-name-when-generating-guide.patch
- Include the datastream versions of Firefox and Java Runtime Environment (JRE) benchmarks
- Include USGCB and DISA STIG profile kickstart files for Red Hat Enterprise Linux 6

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
