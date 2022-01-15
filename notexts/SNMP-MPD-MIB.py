#
# PySNMP MIB module SNMP-MPD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMP-MPD-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:04:41 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, Counter32, snmpModules, IpAddress, Bits, ObjectIdentity, Integer32, ModuleIdentity, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "snmpModules", "IpAddress", "Bits", "ObjectIdentity", "Integer32", "ModuleIdentity", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snmpMPDMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 11))
snmpMPDMIB.setRevisions(('2002-10-14 00:00', '1999-05-04 16:36', '1997-09-30 00:00',))
if mibBuilder.loadTexts: snmpMPDMIB.setLastUpdated('200210140000Z')
if mibBuilder.loadTexts: snmpMPDMIB.setOrganization('SNMPv3 Working Group')
snmpMPDAdmin = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 1))
snmpMPDMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 2))
snmpMPDMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3))
snmpMPDStats = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 2, 1))
snmpUnknownSecurityModels = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnknownSecurityModels.setStatus('current')
snmpInvalidMsgs = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInvalidMsgs.setStatus('current')
snmpUnknownPDUHandlers = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnknownPDUHandlers.setStatus('current')
snmpMPDMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3, 1))
snmpMPDMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3, 2))
snmpMPDCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 11, 3, 1, 1)).setObjects(("SNMP-MPD-MIB", "snmpMPDGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpMPDCompliance = snmpMPDCompliance.setStatus('current')
snmpMPDGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 11, 3, 2, 1)).setObjects(("SNMP-MPD-MIB", "snmpUnknownSecurityModels"), ("SNMP-MPD-MIB", "snmpInvalidMsgs"), ("SNMP-MPD-MIB", "snmpUnknownPDUHandlers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpMPDGroup = snmpMPDGroup.setStatus('current')
mibBuilder.exportSymbols("SNMP-MPD-MIB", snmpUnknownSecurityModels=snmpUnknownSecurityModels, snmpMPDMIB=snmpMPDMIB, snmpMPDMIBCompliances=snmpMPDMIBCompliances, snmpUnknownPDUHandlers=snmpUnknownPDUHandlers, snmpMPDStats=snmpMPDStats, snmpMPDMIBGroups=snmpMPDMIBGroups, PYSNMP_MODULE_ID=snmpMPDMIB, snmpMPDMIBConformance=snmpMPDMIBConformance, snmpMPDAdmin=snmpMPDAdmin, snmpInvalidMsgs=snmpInvalidMsgs, snmpMPDGroup=snmpMPDGroup, snmpMPDMIBObjects=snmpMPDMIBObjects, snmpMPDCompliance=snmpMPDCompliance)
