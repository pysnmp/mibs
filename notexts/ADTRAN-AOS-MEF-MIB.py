#
# PySNMP MIB module ADTRAN-AOS-MEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-MEF-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 16:38:59 2024
# On host fv-az1437-189 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
adGenAOS, adGenAOSMef = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOS", "adGenAOSMef")
adIdentityShared, adShared = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared", "adShared")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Counter32, Counter64, NotificationType, Unsigned32, TimeTicks, iso, ModuleIdentity, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Counter32", "Counter64", "NotificationType", "Unsigned32", "TimeTicks", "iso", "ModuleIdentity", "IpAddress", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAOSMefMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 9))
adGenAOSMefMib.setRevisions(('2014-09-10 00:00',))
if mibBuilder.loadTexts: adGenAOSMefMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAOSMefMib.setOrganization('ADTRAN, Inc.')
adGenAosMefPerUniPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1))
adGenAosMefPerCosPerUniPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2))
adGenAosMefPerEvcPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3))
adGenAosMefPerCosPerEvcPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4))
mibBuilder.exportSymbols("ADTRAN-AOS-MEF-MIB", adGenAosMefPerCosPerEvcPerfHistoryMib=adGenAosMefPerCosPerEvcPerfHistoryMib, adGenAosMefPerCosPerUniPerfHistoryMib=adGenAosMefPerCosPerUniPerfHistoryMib, adGenAosMefPerEvcPerfHistoryMib=adGenAosMefPerEvcPerfHistoryMib, PYSNMP_MODULE_ID=adGenAOSMefMib, adGenAosMefPerUniPerfHistoryMib=adGenAosMefPerUniPerfHistoryMib, adGenAOSMefMib=adGenAOSMefMib)
