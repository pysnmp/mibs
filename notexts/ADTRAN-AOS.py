#
# PySNMP MIB module ADTRAN-AOS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS
# Produced by pysmi-1.1.8 at Tue Jul 26 16:37:54 2022
# On host fv-az119-924 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
adIdentityShared, adShared = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared", "adShared")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Unsigned32, Bits, IpAddress, TimeTicks, MibIdentifier, Counter32, Integer32, iso, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Unsigned32", "Bits", "IpAddress", "TimeTicks", "MibIdentifier", "Counter32", "Integer32", "iso", "Counter64", "ModuleIdentity")
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
mibBuilder.exportSymbols("ADTRAN-AOS", adGenAOSMef=adGenAOSMef, PYSNMP_MODULE_ID=adGenAOSMib, adGenAOSSecurity=adGenAOSSecurity, adGenAOSConformance=adGenAOSConformance, adGenAOSCommon=adGenAOSCommon, adGenAOSApplications=adGenAOSApplications, adGenAOSPower=adGenAOSPower, adGenAOSVoice=adGenAOSVoice, adGenAOS=adGenAOS, adGenAOSRouter=adGenAOSRouter, adGenAOSSwitch=adGenAOSSwitch, adGenAOSMib=adGenAOSMib, adGenAOSWan=adGenAOSWan)
