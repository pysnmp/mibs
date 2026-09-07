#
# PySNMP MIB module ARUBAWIRED-MGMD-RMON-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ARUBAWIRED-MGMD-RMON-TRAP-MIB
# Source digest sha256:65de27dd71131d7633337d1b9354045434ff9988c8dbacdb1d84aa70558e1c93
# Produced by pysmi-2.3.0
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
eventDescription, eventIndex = mibBuilder.importSymbols("RMON-MIB", "eventDescription", "eventIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaWiredMgmdRmonTrapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 4))
arubaWiredMgmdRmonTrapMIB.setRevisions(('2017-11-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setLastUpdated('2017-11-02 00:00')
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setOrganization('HPE/Aruba Networking Division')
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setContactInfo('Hewlett Packard Company\r\n                       8000 Foothills Blvd.\r\n                       Roseville, CA 95747')
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setDescription('This MIB module describes objects to configure\r\n               RMON traps.')
arubaWiredMgmdRmonTrapNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 4, 1))
arubaWiredMgmdRmonTrapEvent = NotificationType((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 4, 1, 1)).setObjects(("RMON-MIB", "eventIndex"), ("RMON-MIB", "eventDescription"))
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapEvent.setStatus('current')
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapEvent.setDescription('The event ID for which the trap is set has occured.')
mibBuilder.exportSymbols("ARUBAWIRED-MGMD-RMON-TRAP-MIB", PYSNMP_MODULE_ID=arubaWiredMgmdRmonTrapMIB, arubaWiredMgmdRmonTrapEvent=arubaWiredMgmdRmonTrapEvent, arubaWiredMgmdRmonTrapMIB=arubaWiredMgmdRmonTrapMIB, arubaWiredMgmdRmonTrapNotifications=arubaWiredMgmdRmonTrapNotifications)
