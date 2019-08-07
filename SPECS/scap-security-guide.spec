%global		redhatssgversion	43

# Somehow, _pkgdocdir is already defined and points to unversioned docs dir
# RHEL 7.X uses versioned docs dir, hence the definition below
%global _pkgdocdir %{_docdir}/%{name}-%{version}

Name:		scap-security-guide
Version:	0.1.%{redhatssgversion}
Release:	13%{?dist}
Summary:	Security guidance and baselines in SCAP formats

Group:		System Environment/Base
License:	BSD-3-Clause
URL:		https://github.com/ComplianceAsCode/content
Source0:	%{name}-%{version}.tar.bz2
Patch1:		scap-security-guide-0.1.44-rule_pcsc-lite_installed.patch
Patch2:		scap-security-guide-0.1.44-fix_no_direct_root_logins_changed_when.patch
Patch3:		scap-security-guide-0.1.44-rules_docker_psacct_installed.patch
Patch4:		scap-security-guide-0.1.44-fix_removed_sebooleans.patch
Patch5:		scap-security-guide-0.1.44-fix_ansible_sssd_tasks.patch
Patch6:		scap-security-guide-0.1.44-template_file_permissions_use_regex.patch
Patch7:		scap-security-guide-0.1.44-fix_rpm_verify_permissions.patch
Patch8:		scap-security-guide-0.1.44-fix_stig_duplicated_audit_rules.patch
Patch9:		scap-security-guide-0.1.45-mark_rules_as_machine_only.patch
Patch10:	scap-security-guide-0.1.44-cpe-shadow-utils.patch
Patch11:	scap-security-guide-0.1.44-cpe-pam-systemd-yum.patch
Patch12:	scap-security-guide-0.1.44-cpe-gdm.patch
Patch13:	scap-security-guide-0.1.44-cpe-remaining.patch
Patch14:	scap-security-guide-0.1.44-update-cpe-dictionary.patch
Patch15:	scap-security-guide-0.1.44-mark_selinux_rules_as_machine_only.patch
Patch16:	scap-security-guide-0.1.44-mark_service_disabled_rules_as_machine_only.patch
Patch17:	scap-security-guide-0.1.44-remove_gpgcheck_repo_from_profiles.patch
Patch18:	scap-security-guide-0.1.44-deduplicate_cce_assigned_to_rules.patch
Patch19:	evaluate_new_package_cpes_to_true.patch
Patch20:	scap-security-guide-0.1.44-deduplicate_cce_assigned_to_rules2.patch
Patch21:	scap-security-guide-0.1.45-fix_rule_sssd_ssh_known_hosts_timeout.patch
Patch22:	add-missing-tags-and-platforms.patch
Patch23:	scap-security-guide-0.1.45-fix_ansible_sssd_ssh_known_hosts_timeout.patch
Patch24:	remove_dconf_use_text_backend_rule_from_profiles.patch
Patch25:	scap-security-guide-0.1.45-aide_not_applicable_to_containers.patch
Patch26:	scap-security-guide-0.1.45-smartcards_not_applicable_to_containers.patch
Patch27:	scap-security-guide-0.1.45-add_rule_dconf_db_up_to_date.patch
Patch28:	scap-security-guide-0.1.45-fix_dconf_remediation.patch
Patch999:       centos-debranding.patch
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
# Workaround to remove Python byte cache files from the upstream sources
# See https://github.com/ComplianceAsCode/content/issues/4042
find . -name '*.pyc' -exec rm -f {} ';'
mkdir build
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
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
%patch999 -p1

%build
mkdir -p build && cd build
%cmake -D CMAKE_INSTALL_DOCDIR=%{_pkgdocdir} \
-DSSG_PRODUCT_EXAMPLE:BOOL=OFF \
-DSSG_PRODUCT_CHROMIUM:BOOL=OFF \
-DSSG_PRODUCT_DEBIAN8:BOOL=OFF \
-DSSG_PRODUCT_FEDORA:BOOL=OFF \
-DSSG_PRODUCT_FIREFOX:BOOL=ON \
-DSSG_PRODUCT_JBOSS_EAP6:BOOL=OFF \
-DSSG_PRODUCT_JBOSS_FUSE6:BOOL=OFF \
-DSSG_PRODUCT_JBOSS_JRE:BOOL=ON \
-DSSG_PRODUCT_OCP3:BOOL=OFF \
-DSSG_PRODUCT_OPENSUSE:BOOL=OFF \
-DSSG_PRODUCT_OSP13:BOOL=OFF \
-DSSG_PRODUCT_RHEL6:BOOL=ON \
-DSSG_PRODUCT_RHEL7:BOOL=ON \
-DSSG_PRODUCT_RHEL8:BOOL=OFF \
-DSSG_PRODUCT_RHV4:BOOL=OFF \
-DSSG_PRODUCT_SUSE11:BOOL=OFF \
-DSSG_PRODUCT_SUSE12:BOOL=OFF \
-DSSG_PRODUCT_UBUNTU14:BOOL=OFF \
-DSSG_PRODUCT_UBUNTU16:BOOL=OFF \
-DSSG_PRODUCT_UBUNTU18:BOOL=OFF \
-DSSG_PRODUCT_WRLINUX:BOOL=OFF \
-DSSG_PRODUCT_OL7:BOOL=OFF \
-DSSG_PRODUCT_OL8:BOOL=OFF \
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
* Wed Jun 12 2019 Matěj Týč <matyc@redhat.com> - 0.1.43-13
- Fixed the shared dconf bash remediation (RHBZ#1631378)

* Mon Jun 03 2019 Jan Černý <jcerny@redhat.com> - 0.1.43-12
- Make aide and smart card rules not applicable to containers (RHBZ#1711893)
- Added rule dconf_db_up_to_date to ensure dconf databases are up-to-date (RHBZ#1631378)

* Fri May 24 2019 Gabriel Becker <ggasparb@redhat.com> - 0.1.43-11
- Remove faulty dconf_use_text_backend rule from all profiles (Reverts RHBZ#1631378)

* Thu May 23 2019 Gabriel Becker <ggasparb@redhat.com> - 0.1.43-10
- Fixed Ansible remediation for sssd_ssh_known_hosts_timeout (RHBZ#1599179)

* Mon May 20 2019 Jan Černý <jcerny@redhat.com> - 0.1.43-9
- Fixed missing Ansible tags and platform checks (RHBZ#1685950)

* Fri May 17 2019 Gabriel Becker <ggasparb@redhat.com> - 0.1.43-8
- Fixed OVAL check for sssd_ssh_known_hosts_timeout and added bash remediation (RHBZ#1599179)

* Fri May 10 2019 Watson Yuuma Sato <wsato@redhat.com> - 0.1.43-7
- Fix handling of package CPE during generation of Ansible playbooks (RHBZ#1647189)

* Fri May 10 2019 Watson Yuuma Sato <wsato@redhat.com> - 0.1.43-6
- Deduplicated more CCEs assigned to rules (RHBZ#1703092)

* Thu Apr 25 2019 Gabriel Becker <ggasparb@redhat.com> - 0.1.43-5
- Remove ensure_gpgcheck_repo_metadata rule from profiles (RHBZ#1703010)
- Deduplicate CCE assigned to rules (RHBZ#1703092)

* Tue Apr 23 2019 Gabriel Becker <ggasparb@redhat.com> - 0.1.43-4
- Mark SELinux rules as machine only (RHBZ#1630739)
- Mark service disabled rules as machine only (RHBZ#1630739)

* Mon Apr 08 2019 Gabriel Becker <ggasparb@redhat.com> - 0.1.43-3
- Mark rules which were not applicable for containers as machine only (RHBZ#1630739)
- Fix content support for UBI-Minimal (RHBZ#1695213)

* Mon Mar 25 2019 Watson Yuuma Sato <wsato@redhat.com> - 0.1.43-2
- Fixes for smooth Ansible playbooks run (RHBZ#1647189)
- Fix Ansible template for file permissions (RHBZ#1686007)
- Fix remediation of rule rpm_verify_permissions (RHBZ#1686005)
- Fix remediation of audit rules for privileged commands (RHBZ#1687826)

* Fri Mar 01 2019 Jan Černý <jcerny@redhat.com> - 0.1.43-1
- Update to the latest upstream release (RHBZ#1684545)

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
