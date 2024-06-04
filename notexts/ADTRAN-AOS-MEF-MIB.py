#
# PySNMP MIB module ADTRAN-AOS-MEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-MEF-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:14:03 2024
# On host fv-az1385-751 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
adGenAOSMef, adGenAOS = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSMef", "adGenAOS")
adIdentityShared, adShared = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared", "adShared")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, Integer32, IpAddress, Counter64, iso, NotificationType, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Integer32", "IpAddress", "Counter64", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "Gauge32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSMefMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 9))
adGenAOSMefMib.setRevisions(('2014-09-10 00:00',))
if mibBuilder.loadTexts: adGenAOSMefMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAOSMefMib.setOrganization('ADTRAN, Inc.')
adGenAosMefPerUniPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1))
adGenAosMefPerCosPerUniPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2))
adGenAosMefPerEvcPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3))
adGenAosMefPerCosPerEvcPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4))
mibBuilder.exportSymbols("ADTRAN-AOS-MEF-MIB", adGenAOSMefMib=adGenAOSMefMib, adGenAosMefPerEvcPerfHistoryMib=adGenAosMefPerEvcPerfHistoryMib, adGenAosMefPerCosPerEvcPerfHistoryMib=adGenAosMefPerCosPerEvcPerfHistoryMib, adGenAosMefPerCosPerUniPerfHistoryMib=adGenAosMefPerCosPerUniPerfHistoryMib, adGenAosMefPerUniPerfHistoryMib=adGenAosMefPerUniPerfHistoryMib, PYSNMP_MODULE_ID=adGenAOSMefMib)
