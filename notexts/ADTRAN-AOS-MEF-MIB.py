#
# PySNMP MIB module ADTRAN-AOS-MEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-MEF-MIB
# Produced by pysmi-1.1.12 at Thu Nov 28 02:54:09 2024
# On host fv-az885-149 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
adGenAOS, adGenAOSMef = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOS", "adGenAOSMef")
adShared, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adShared", "adIdentityShared")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Counter64, ObjectIdentity, Integer32, NotificationType, MibIdentifier, iso, TimeTicks, Bits, IpAddress, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Counter64", "ObjectIdentity", "Integer32", "NotificationType", "MibIdentifier", "iso", "TimeTicks", "Bits", "IpAddress", "Unsigned32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSMefMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 9))
adGenAOSMefMib.setRevisions(('2014-09-10 00:00',))
if mibBuilder.loadTexts: adGenAOSMefMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAOSMefMib.setOrganization('ADTRAN, Inc.')
adGenAosMefPerUniPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1))
adGenAosMefPerCosPerUniPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2))
adGenAosMefPerEvcPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3))
adGenAosMefPerCosPerEvcPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4))
mibBuilder.exportSymbols("ADTRAN-AOS-MEF-MIB", adGenAosMefPerEvcPerfHistoryMib=adGenAosMefPerEvcPerfHistoryMib, adGenAosMefPerCosPerUniPerfHistoryMib=adGenAosMefPerCosPerUniPerfHistoryMib, adGenAOSMefMib=adGenAOSMefMib, adGenAosMefPerCosPerEvcPerfHistoryMib=adGenAosMefPerCosPerEvcPerfHistoryMib, PYSNMP_MODULE_ID=adGenAOSMefMib, adGenAosMefPerUniPerfHistoryMib=adGenAosMefPerUniPerfHistoryMib)
