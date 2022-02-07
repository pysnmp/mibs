#
# PySNMP MIB module IANA-LANGUAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-LANGUAGE-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:06:13 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, Counter64, MibIdentifier, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Integer32, NotificationType, IpAddress, iso, ObjectIdentity, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Counter64", "MibIdentifier", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Integer32", "NotificationType", "IpAddress", "iso", "ObjectIdentity", "mib-2")
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
mibBuilder.exportSymbols("IANA-LANGUAGE-MIB", ianaLangSMSL=ianaLangSMSL, PYSNMP_MODULE_ID=ianaLanguages, ianaLangScheme=ianaLangScheme, ianaLangPSL=ianaLangPSL, ianaLangSRSL=ianaLangSRSL, ianaLangPerl=ianaLangPerl, ianaLanguages=ianaLanguages, ianaLangJavaByteCode=ianaLangJavaByteCode, ianaLangTcl=ianaLangTcl)
