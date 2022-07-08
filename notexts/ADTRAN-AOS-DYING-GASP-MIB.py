#
# PySNMP MIB module ADTRAN-AOS-DYING-GASP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-DYING-GASP-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:20:08 2022
# On host fv-az130-744 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
adGenAOSConformance, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSCommon")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, ModuleIdentity, Bits, Counter32, Counter64, iso, IpAddress, MibIdentifier, Integer32, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Bits", "Counter32", "Counter64", "iso", "IpAddress", "MibIdentifier", "Integer32", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSDyingGaspMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 11))
adGenAOSDyingGaspMib.setRevisions(('2015-01-05 00:00',))
if mibBuilder.loadTexts: adGenAOSDyingGaspMib.setLastUpdated('201501050000Z')
if mibBuilder.loadTexts: adGenAOSDyingGaspMib.setOrganization('ADTRAN, Inc.')
adGenAOSDyingGasp = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 11))
adGenAOSDyingGaspTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 11, 0))
adGenAOSDyingGaspEvent = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 11, 0, 1))
if mibBuilder.loadTexts: adGenAOSDyingGaspEvent.setStatus('current')
adGenAOSDyingGaspConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25))
adGenAOSDyingGaspGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25, 1))
adGenAOSDyingGaspCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25, 2))
adGenAOSDyingGaspFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25, 2, 1)).setObjects(("ADTRAN-AOS-DYING-GASP-MIB", "adGenAOSDyingGaspGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSDyingGaspFullCompliance = adGenAOSDyingGaspFullCompliance.setStatus('current')
adGenAOSDyingGaspGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25, 1, 1)).setObjects(("ADTRAN-AOS-DYING-GASP-MIB", "adGenAOSDyingGaspEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSDyingGaspGroup = adGenAOSDyingGaspGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-DYING-GASP-MIB", adGenAOSDyingGaspCompliances=adGenAOSDyingGaspCompliances, adGenAOSDyingGaspConformance=adGenAOSDyingGaspConformance, adGenAOSDyingGaspEvent=adGenAOSDyingGaspEvent, adGenAOSDyingGaspGroups=adGenAOSDyingGaspGroups, PYSNMP_MODULE_ID=adGenAOSDyingGaspMib, adGenAOSDyingGaspGroup=adGenAOSDyingGaspGroup, adGenAOSDyingGasp=adGenAOSDyingGasp, adGenAOSDyingGaspMib=adGenAOSDyingGaspMib, adGenAOSDyingGaspFullCompliance=adGenAOSDyingGaspFullCompliance, adGenAOSDyingGaspTrap=adGenAOSDyingGaspTrap)
