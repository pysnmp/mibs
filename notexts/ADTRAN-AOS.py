#
# PySNMP MIB module ADTRAN-AOS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS
# Produced by pysmi-1.1.12 at Tue Jun  4 13:29:11 2024
# On host fv-az573-215 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
adIdentityShared, adShared = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared", "adShared")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, NotificationType, iso, Counter64, ModuleIdentity, TimeTicks, Counter32, MibIdentifier, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "NotificationType", "iso", "Counter64", "ModuleIdentity", "TimeTicks", "Counter32", "MibIdentifier", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ADTRAN-AOS", adGenAOSSecurity=adGenAOSSecurity, adGenAOSSwitch=adGenAOSSwitch, adGenAOSConformance=adGenAOSConformance, adGenAOSVoice=adGenAOSVoice, PYSNMP_MODULE_ID=adGenAOSMib, adGenAOSRouter=adGenAOSRouter, adGenAOSPower=adGenAOSPower, adGenAOSMef=adGenAOSMef, adGenAOS=adGenAOS, adGenAOSMib=adGenAOSMib, adGenAOSCommon=adGenAOSCommon, adGenAOSApplications=adGenAOSApplications, adGenAOSWan=adGenAOSWan)
