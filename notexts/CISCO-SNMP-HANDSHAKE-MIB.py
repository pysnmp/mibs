#
# PySNMP MIB module CISCO-SNMP-HANDSHAKE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SNMP-HANDSHAKE-MIB
# Source digest sha256:022471601ad2b8ee2a9a88e7489bef797780510ade2f2e9d8d908fcda234459f
# Produced by pysmi-2.3.0
#
bsnWireless, = mibBuilder.importSymbols("AIRESPACE-WIRELESS-MIB", "bsnWireless")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoSnmpHandshakeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14179, 2, 40))
ciscoSnmpHandshakeMIB.setRevisions(('2007-05-23 00:00',))
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setLastUpdated('2007-05-23 00:00')
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setOrganization('Cisco Systems Inc.')
ciscoSnmpHandshakeMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 0))
ciscoSnmpHandshakeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1))
ciscoSnmpHandshakeMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2))
ciscoSnmpHandshakeProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1))
ciscoSnmpHandshakeTest = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 2))
csHandshakeInit = MibScalar((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: csHandshakeInit.setStatus('current')
csHandshakeUpdate = MibScalar((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csHandshakeUpdate.setStatus('current')
csHandshakeCheck = MibScalar((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 2, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csHandshakeCheck.setStatus('current')
ciscoSnmpHandshakeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 1))
ciscoSnmpHandshakeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 2))
ciscoSnmpHandshakeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 1, 1)).setObjects(("CISCO-SNMP-HANDSHAKE-MIB", "ciscoSnmpHandshakeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpHandshakeMIBCompliance = ciscoSnmpHandshakeMIBCompliance.setStatus('current')
ciscoSnmpHandshakeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 2, 1)).setObjects(("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeInit"), ("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeUpdate"), ("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeCheck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpHandshakeGroup = ciscoSnmpHandshakeGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-HANDSHAKE-MIB", PYSNMP_MODULE_ID=ciscoSnmpHandshakeMIB, ciscoSnmpHandshakeGroup=ciscoSnmpHandshakeGroup, ciscoSnmpHandshakeMIB=ciscoSnmpHandshakeMIB, ciscoSnmpHandshakeMIBCompliance=ciscoSnmpHandshakeMIBCompliance, ciscoSnmpHandshakeMIBCompliances=ciscoSnmpHandshakeMIBCompliances, ciscoSnmpHandshakeMIBConform=ciscoSnmpHandshakeMIBConform, ciscoSnmpHandshakeMIBGroups=ciscoSnmpHandshakeMIBGroups, ciscoSnmpHandshakeMIBNotifs=ciscoSnmpHandshakeMIBNotifs, ciscoSnmpHandshakeMIBObjects=ciscoSnmpHandshakeMIBObjects, ciscoSnmpHandshakeProcess=ciscoSnmpHandshakeProcess, ciscoSnmpHandshakeTest=ciscoSnmpHandshakeTest, csHandshakeCheck=csHandshakeCheck, csHandshakeInit=csHandshakeInit, csHandshakeUpdate=csHandshakeUpdate)
