#
# PySNMP MIB module ADTRAN-AOS-MEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-MEF-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 19:18:03 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adGenAOSMef, adGenAOS = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSMef", "adGenAOS")
adShared, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adShared", "adIdentityShared")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, Gauge32, Counter64, Bits, Unsigned32, Integer32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Gauge32", "Counter64", "Bits", "Unsigned32", "Integer32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSMefMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 9))
adGenAOSMefMib.setRevisions(('2014-09-10 00:00',))
if mibBuilder.loadTexts: adGenAOSMefMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAOSMefMib.setOrganization('ADTRAN, Inc.')
adGenAosMefPerUniPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1))
adGenAosMefPerCosPerUniPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2))
adGenAosMefPerEvcPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3))
adGenAosMefPerCosPerEvcPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4))
mibBuilder.exportSymbols("ADTRAN-AOS-MEF-MIB", adGenAosMefPerUniPerfHistoryMib=adGenAosMefPerUniPerfHistoryMib, adGenAosMefPerCosPerUniPerfHistoryMib=adGenAosMefPerCosPerUniPerfHistoryMib, adGenAosMefPerEvcPerfHistoryMib=adGenAosMefPerEvcPerfHistoryMib, adGenAosMefPerCosPerEvcPerfHistoryMib=adGenAosMefPerCosPerEvcPerfHistoryMib, PYSNMP_MODULE_ID=adGenAOSMefMib, adGenAOSMefMib=adGenAOSMefMib)
