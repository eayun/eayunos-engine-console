Name:		eayunos-engine-console
Version:	0.8
Release:	11%{?dist}
Summary:	Management Tool

Group:		Application
License:	GPL
URL:		http://www.eayun.com
Source0:	eayunos-engine-console-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	/bin/bash
Requires:	ovirt-engine
Requires:	engine-reports-config-passwd

%description
EayunOS Engine Management Tool.

%prep
%setup -q


%build


%install
rm -rf %{buildroot}
rm -rf .git
mkdir -p %{buildroot}/usr/libexec/
mkdir -p %{buildroot}/usr/share/doc/eayunos-engine-console/
mkdir -p %{buildroot}/usr/share/eayunos-engine-console/bin/
cp eayunos-engine-console %{buildroot}/usr/libexec/
cp README.md %{buildroot}/usr/share/doc/eayunos-engine-console/
cp HELP.md %{buildroot}/usr/share/doc/eayunos-engine-console/
cp bin/ovirt-reset-db-password %{buildroot}/usr/share/eayunos-engine-console/bin/

%post
useradd engineadm &> /dev/null
passwd -d engineadm &> /dev/null
passwd -e engineadm &> /dev/null
sed -i "/engineadm/ s/\/bin\/bash/\/usr\/libexec\/eayunos-engine-console/g" /etc/passwd
echo 'engineadm   ALL=(ALL)       NOPASSWD:ALL' >> /etc/sudoers
cat >> /etc/rsyslog.conf <<EOF
# Save eayunos-engine-console messages
local3.*                                                /var/log/eayunos-engine-console.log
EOF
service rsyslog restart &> /dev/null
ln -s /usr/share/eayunos-engine-console/bin/ovirt-reset-db-password /usr/bin/ovirt-reset-db-password

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%attr(0755,root,root)/usr/libexec/eayunos-engine-console
%attr(0755,root,root)/usr/share/eayunos-engine-console/bin/ovirt-reset-db-password
%doc /usr/share/doc/eayunos-engine-console/README.md
%doc /usr/share/doc/eayunos-engine-console/HELP.md




%changelog
* Fri Dec 26 2014 MaZhe <zhe.ma@eayun.com> 0.8-11
- Fixed issue #24

* Tue Dec 23 2014 MaZhe <zhe.ma@eayun.com> 0.8-10
- Fixed issue #23

* Tue Dec 23 2014 MaZhe <zhe.ma@eayun.com> 0.8-9
- Code optimization

* Tue Dec 23 2014 MaZhe <zhe.ma@eayun.com> 0.8-8
- Code optimization

* Wed Dec 17 2014 MaZhe <zhe.ma@eayun.com> 0.8-7
- Fix isodomain "WGT_DOMAIN" initialization failed bug
  Bug fix [issue #23]

* Fri Dec 12 2014 MaZhe <zhe.ma@eayun.com> 0.8-6
- Update README & HELP Docment

* Fri Dec 12 2014 MaZhe <zhe.ma@eayun.com> 0.8-5
- Add update reports service configuration files function
  Resolve [issue #21]

* Thu Dec 11 2014 MaZhe <zhe.ma@eayun.com> 0.8-4
- Bug fix

* Thu Dec 11 2014 MaZhe <zhe.ma@eayun.com> 0.8-3
- Add update reports configuration file function

* Thu Dec 11 2014 MaZhe <zhe.ma@eayun.com> 0.8-2
- Update README & HELP

* Wed Dec 10 2014 MaZhe <zhe.ma@eayun.com> 0.8-1
- Add reset database user's password function

* Wed Dec 10 2014 MaZhe <zhe.ma@eayun.com> 0.7-2
- Code optimization

* Wed Dec 10 2014 MaZhe <zhe.ma@eayun.com> 0.7-1
- Update engine-manage-domains/ovirt-optimizer/engine-vm-backup configuration 
  when reset IP/HOSTNAME/admin user's password
  Resolve [issue #19]

* Tue Dec  9 2014 MaZhe <zhe.ma@eayun.com> 0.6-6
- Resolve the garbled problem [issue #17]
  Code optimization
  Add update ovirt-optimizer.properties file function [issue #18]
  

* Thu Dec  4 2014 MaZhe <zhe.ma@eayun.com> 0.6-5
- Resolve issue [issue #16]

* Thu Dec  4 2014 MaZhe <zhe.ma@eayun.com> 0.6-4
- Modify misspelled words
  Fix issue [issue #14]

* Mon Dec  1 2014 MaZhe <zhe.ma@eayun.com> 0.6-3
- Modify rename parameter "confirmForceOverwrite" to True
- Resolve issue [issue #13]

* Mon Dec  1 2014 MaZhe <zhe.ma@eayun.com> 0.6-2
- Modify ENGINE_REPORTS_BASE_URL by rename function

* Fri Nov 28 2014 MaZhe <zhe.ma@eayun.com> 0.6-1
- Added a function to display HELP information

* Fri Nov 28 2014 MaZhe <zhe.ma@eayun.com> 0.5-6
- Added a function to display the password of the admin user of the reports portal [issue #12]

* Fri Nov 27 2014 MaZhe <zhe.ma@eayun.com> 0.5-5
- Fix string compare bug [issue #8]

* Fri Nov 27 2014 MaZhe <zhe.ma@eayun.com> 0.5-4
- Resolve hostname revert to "localhost" issue [issue #3]

* Fri Nov 26 2014 MaZhe <zhe.ma@eayun.com> 0.5-3
- Resolve hostname configuration issue [issue #5]

* Fri Nov 26 2014 MaZhe <zhe.ma@eayun.com> 0.5-2
- Fix network configuration bug [issue #6]

* Fri Nov 26 2014 MaZhe <zhe.ma@eayun.com> 0.5-1
- Add oVirt Engine Reports Portal user password configuration function

* Fri Nov 21 2014 MaZhe <zhe.ma@eayun.com> 0.4-6
- fix interactive infomation (issues #2)

* Fri Oct 17 2014 MaZhe <zhe.ma@eayun.com> 0.1-1
- Initial package tagging.
