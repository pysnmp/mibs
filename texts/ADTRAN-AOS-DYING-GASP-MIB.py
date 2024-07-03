#
# PySNMP MIB module ADTRAN-AOS-DYING-GASP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-DYING-GASP-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 09:07:37 2024
# On host fv-az2021-432 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
adGenAOSConformance, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSCommon")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Bits, MibIdentifier, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, ObjectIdentity, Unsigned32, IpAddress, Counter64, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "MibIdentifier", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSDyingGaspMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 11))
adGenAOSDyingGaspMib.setRevisions(('2015-01-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSDyingGaspMib.setRevisionsDescriptions(('Created the adGenAosDyingGasp MIB. Revision R11.6',))
if mibBuilder.loadTexts: adGenAOSDyingGaspMib.setLastUpdated('201501050000Z')
if mibBuilder.loadTexts: adGenAOSDyingGaspMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSDyingGaspMib.setContactInfo('        Technical Support Dept.\n                    Postal: ADTRAN, Inc.\n                    901 Explorer Blvd.\n                    Huntsville, AL 35806\n\n               Tel: +1 800 726-8663\n               Fax: +1 256 963 6217\n            E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSDyingGaspMib.setDescription('The MIB module defines dying gasp traps for AdtranOS products.')
adGenAOSDyingGasp = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 11))
adGenAOSDyingGaspTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 11, 0))
adGenAOSDyingGaspEvent = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 11, 0, 1))
if mibBuilder.loadTexts: adGenAOSDyingGaspEvent.setStatus('current')
if mibBuilder.loadTexts: adGenAOSDyingGaspEvent.setDescription('A dying gasp event trap signifies that the unit has unexpectedly lost power.')
adGenAOSDyingGaspConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25))
adGenAOSDyingGaspGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25, 1))
adGenAOSDyingGaspCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25, 2))
adGenAOSDyingGaspFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25, 2, 1)).setObjects(("ADTRAN-AOS-DYING-GASP-MIB", "adGenAOSDyingGaspGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSDyingGaspFullCompliance = adGenAOSDyingGaspFullCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAOSDyingGaspFullCompliance.setDescription('The compliance statement for SNMP entities which implement\n        version 2 of the adGenAosDyingGasp MIB. When the implementation of this MIB \n        supports adGenAOSDyingGaspGroup, then such an implementation can claim\n        full compliance.')
adGenAOSDyingGaspGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 25, 1, 1)).setObjects(("ADTRAN-AOS-DYING-GASP-MIB", "adGenAOSDyingGaspEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSDyingGaspGroup = adGenAOSDyingGaspGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSDyingGaspGroup.setDescription('Trap which may be used to indicate an unexpected power loss of the system.')
mibBuilder.exportSymbols("ADTRAN-AOS-DYING-GASP-MIB", adGenAOSDyingGaspMib=adGenAOSDyingGaspMib, adGenAOSDyingGaspTrap=adGenAOSDyingGaspTrap, adGenAOSDyingGasp=adGenAOSDyingGasp, adGenAOSDyingGaspEvent=adGenAOSDyingGaspEvent, adGenAOSDyingGaspCompliances=adGenAOSDyingGaspCompliances, adGenAOSDyingGaspGroup=adGenAOSDyingGaspGroup, adGenAOSDyingGaspGroups=adGenAOSDyingGaspGroups, adGenAOSDyingGaspConformance=adGenAOSDyingGaspConformance, adGenAOSDyingGaspFullCompliance=adGenAOSDyingGaspFullCompliance, PYSNMP_MODULE_ID=adGenAOSDyingGaspMib)
