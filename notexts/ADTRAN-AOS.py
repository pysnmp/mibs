#
# PySNMP MIB module ADTRAN-AOS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS
# Produced by pysmi-1.1.12 at Tue Dec  3 11:36:25 2024
# On host fv-az842-370 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
adShared, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adShared", "adIdentityShared")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, Unsigned32, IpAddress, Bits, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, NotificationType, ObjectIdentity, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "Unsigned32", "IpAddress", "Bits", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53))
adGenAOSMib.setRevisions(('2014-09-10 00:00', '2012-04-27 00:00', '2010-07-05 00:00', '2004-10-20 00:00',))
if mibBuilder.loadTexts: adGenAOSMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAOSMib.setOrganization('ADTRAN, Inc.')
adGenAOS = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53))
adGenAOSCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1))
adGenAOSRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 2))
adGenAOSSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 3))
adGenAOSSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4))
adGenAOSVoice = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5))
adGenAOSWan = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 6))
adGenAOSPower = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 7))
adGenAOSConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99))
adGenAOSApplications = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 8))
adGenAOSMef = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9))
mibBuilder.exportSymbols("ADTRAN-AOS", adGenAOSMib=adGenAOSMib, adGenAOSMef=adGenAOSMef, PYSNMP_MODULE_ID=adGenAOSMib, adGenAOSSwitch=adGenAOSSwitch, adGenAOSWan=adGenAOSWan, adGenAOSSecurity=adGenAOSSecurity, adGenAOSConformance=adGenAOSConformance, adGenAOS=adGenAOS, adGenAOSCommon=adGenAOSCommon, adGenAOSRouter=adGenAOSRouter, adGenAOSVoice=adGenAOSVoice, adGenAOSApplications=adGenAOSApplications, adGenAOSPower=adGenAOSPower)
