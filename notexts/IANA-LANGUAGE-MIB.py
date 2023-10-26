#
# PySNMP MIB module IANA-LANGUAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-LANGUAGE-MIB
# Produced by pysmi-1.1.8 at Thu Oct 26 08:54:53 2023
# On host fv-az1032-268 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, mib_2, MibIdentifier, ModuleIdentity, ObjectIdentity, TimeTicks, NotificationType, Integer32, IpAddress, Bits, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "mib-2", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "NotificationType", "Integer32", "IpAddress", "Bits", "iso", "Gauge32")
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
mibBuilder.exportSymbols("IANA-LANGUAGE-MIB", ianaLangSMSL=ianaLangSMSL, PYSNMP_MODULE_ID=ianaLanguages, ianaLangTcl=ianaLangTcl, ianaLangJavaByteCode=ianaLangJavaByteCode, ianaLangScheme=ianaLangScheme, ianaLangSRSL=ianaLangSRSL, ianaLangPerl=ianaLangPerl, ianaLanguages=ianaLanguages, ianaLangPSL=ianaLangPSL)
