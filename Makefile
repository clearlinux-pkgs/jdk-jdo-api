PKG_NAME := jdk-jdo-api
URL := https://repo1.maven.org/maven2/javax/jdo/jdo-api/3.0.1/jdo-api-3.0.1.jar
ARCHIVES := https://repo1.maven.org/maven2/javax/jdo/jdo-api/3.0.1/jdo-api-3.0.1.pom %{buildroot}

include ../common/Makefile.common
