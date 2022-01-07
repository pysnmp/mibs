#
# PySNMP MIB module IANA-LANGUAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IANA-LANGUAGE-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 00:53:09 2022
# On host fv-az74-997 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Unsigned32, iso, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, MibIdentifier, ModuleIdentity, Counter32, Counter64, mib_2, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Unsigned32", "iso", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "MibIdentifier", "ModuleIdentity", "Counter32", "Counter64", "mib-2", "TimeTicks")
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
mibBuilder.exportSymbols("IANA-LANGUAGE-MIB", ianaLangPSL=ianaLangPSL, ianaLangTcl=ianaLangTcl, ianaLangJavaByteCode=ianaLangJavaByteCode, ianaLangPerl=ianaLangPerl, PYSNMP_MODULE_ID=ianaLanguages, ianaLangScheme=ianaLangScheme, ianaLanguages=ianaLanguages, ianaLangSRSL=ianaLangSRSL, ianaLangSMSL=ianaLangSMSL)
