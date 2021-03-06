Name     : jdk-jdo-api
Version  : 3.0.1
Release  : 4
URL      : https://repo1.maven.org/maven2/javax/jdo/jdo-api/3.0.1/jdo-api-3.0.1.jar
Source0  : https://repo1.maven.org/maven2/javax/jdo/jdo-api/3.0.1/jdo-api-3.0.1.jar
Source1  : https://repo1.maven.org/maven2/javax/jdo/jdo-api/3.0.1/jdo-api-3.0.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-jdo-api-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-jdo-api package.
Group: Data

%description data
data components for the jdk-jdo-api package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/jdo-api.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/jdo-api.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/jdo-api.xml \
%{buildroot}/usr/share/maven-poms/jdo-api.pom \
%{buildroot}/usr/share/java/jdo-api.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/jdo-api.jar
/usr/share/maven-metadata/jdo-api.xml
/usr/share/maven-poms/jdo-api.pom
