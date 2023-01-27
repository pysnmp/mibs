#
# PySNMP MIB module ADTRAN-AOS-DYING-GASP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-DYING-GASP-MIB
# Produced by pysmi-1.1.8 at Fri Jan 27 13:59:31 2023
# On host fv-az417-962 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
adGenAOSConformance, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSCommon")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Gauge32, TimeTicks, MibIdentifier, ObjectIdentity, Bits, NotificationType, Unsigned32, Counter64, ModuleIdentity, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Bits", "NotificationType", "Unsigned32", "Counter64", "ModuleIdentity", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
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
mibBuilder.exportSymbols("ADTRAN-AOS-DYING-GASP-MIB", adGenAOSDyingGaspEvent=adGenAOSDyingGaspEvent, adGenAOSDyingGaspFullCompliance=adGenAOSDyingGaspFullCompliance, adGenAOSDyingGaspConformance=adGenAOSDyingGaspConformance, adGenAOSDyingGaspGroup=adGenAOSDyingGaspGroup, adGenAOSDyingGaspGroups=adGenAOSDyingGaspGroups, adGenAOSDyingGaspMib=adGenAOSDyingGaspMib, PYSNMP_MODULE_ID=adGenAOSDyingGaspMib, adGenAOSDyingGaspCompliances=adGenAOSDyingGaspCompliances, adGenAOSDyingGaspTrap=adGenAOSDyingGaspTrap, adGenAOSDyingGasp=adGenAOSDyingGasp)
