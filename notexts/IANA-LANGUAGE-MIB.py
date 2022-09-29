#
# PySNMP MIB module IANA-LANGUAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-LANGUAGE-MIB
# Produced by pysmi-1.1.8 at Thu Sep 29 12:07:58 2022
# On host fv-az619-657 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, mib_2, Unsigned32, Integer32, IpAddress, ObjectIdentity, Counter32, Counter64, iso, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "mib-2", "Unsigned32", "Integer32", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "iso", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaLanguages = ModuleIdentity((1, 3, 6, 1, 2, 1, 73))
ianaLanguages.setRevisions(('2014-05-22 00:00', '2000-05-10 00:00', '1999-09-09 09:00',))
if mibBuilder.loadTexts: ianaLanguages.setLastUpdated('201405220000Z')
if mibBuilder.loadTexts: ianaLanguages.setOrganization('IANA')
ianaLangJavaByteCode = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 1))
if mibBuilder.loadTexts: ianaLangJavaByteCode.setStatus('current')
ianaLangTcl = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 2))
if mibBuilder.loadTexts: ianaLangTcl.setStatus('current')
ianaLangPerl = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 3))
if mibBuilder.loadTexts: ianaLangPerl.setStatus('current')
ianaLangScheme = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 4))
if mibBuilder.loadTexts: ianaLangScheme.setStatus('current')
ianaLangSRSL = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 5))
if mibBuilder.loadTexts: ianaLangSRSL.setStatus('current')
ianaLangPSL = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 6))
if mibBuilder.loadTexts: ianaLangPSL.setStatus('current')
ianaLangSMSL = ObjectIdentity((1, 3, 6, 1, 2, 1, 73, 7))
if mibBuilder.loadTexts: ianaLangSMSL.setStatus('current')
mibBuilder.exportSymbols("IANA-LANGUAGE-MIB", ianaLanguages=ianaLanguages, ianaLangScheme=ianaLangScheme, ianaLangJavaByteCode=ianaLangJavaByteCode, ianaLangSRSL=ianaLangSRSL, ianaLangPerl=ianaLangPerl, PYSNMP_MODULE_ID=ianaLanguages, ianaLangTcl=ianaLangTcl, ianaLangSMSL=ianaLangSMSL, ianaLangPSL=ianaLangPSL)
