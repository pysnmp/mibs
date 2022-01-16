#
# PySNMP MIB module ADTRAN-AOS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS
# Produced by pysmi-1.1.8 at Sun Jan 16 00:53:55 2022
# On host fv-az74-933 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adShared, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adShared", "adIdentityShared")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, Integer32, Unsigned32, TimeTicks, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, ObjectIdentity, NotificationType, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Integer32", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "ObjectIdentity", "NotificationType", "Counter64", "Counter32")
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
mibBuilder.exportSymbols("ADTRAN-AOS", adGenAOSCommon=adGenAOSCommon, adGenAOSSwitch=adGenAOSSwitch, adGenAOSVoice=adGenAOSVoice, adGenAOSRouter=adGenAOSRouter, adGenAOSApplications=adGenAOSApplications, adGenAOS=adGenAOS, adGenAOSMef=adGenAOSMef, adGenAOSMib=adGenAOSMib, PYSNMP_MODULE_ID=adGenAOSMib, adGenAOSSecurity=adGenAOSSecurity, adGenAOSPower=adGenAOSPower, adGenAOSConformance=adGenAOSConformance, adGenAOSWan=adGenAOSWan)
