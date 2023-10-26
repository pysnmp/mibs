#
# PySNMP MIB module IANA-LANGUAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-LANGUAGE-MIB
# Produced by pysmi-1.1.10 at Thu Oct 26 13:34:15 2023
# On host fv-az306-641 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, Integer32, iso, Counter32, Counter64, NotificationType, Unsigned32, ObjectIdentity, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, mib_2, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Integer32", "iso", "Counter32", "Counter64", "NotificationType", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "mib-2", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("IANA-LANGUAGE-MIB", ianaLangTcl=ianaLangTcl, PYSNMP_MODULE_ID=ianaLanguages, ianaLanguages=ianaLanguages, ianaLangScheme=ianaLangScheme, ianaLangPSL=ianaLangPSL, ianaLangSRSL=ianaLangSRSL, ianaLangPerl=ianaLangPerl, ianaLangSMSL=ianaLangSMSL, ianaLangJavaByteCode=ianaLangJavaByteCode)
