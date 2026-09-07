#
# PySNMP MIB module CISCO-IETF-VPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IETF-VPLS-LDP-MIB
# Source digest sha256:b463ab0726819778b74d097317ff4aecaa29e768f8574c787fc7465fa1b75385
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
cvplsConfigIndex, cvplsPwBindIndex = mibBuilder.importSymbols("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex", "cvplsPwBindIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
VPNId, = mibBuilder.importSymbols("VPN-TC-STD-MIB", "VPNId")
cvplsLdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 141))
cvplsLdpMIB.setRevisions(('2007-11-22 12:00',))
if mibBuilder.loadTexts: cvplsLdpMIB.setLastUpdated('2007-11-22 12:00')
if mibBuilder.loadTexts: cvplsLdpMIB.setOrganization('Cisco Systems, Inc.')
cvplsLdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 1))
cvplsLdpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2))
cvplsLdpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvplsLdpConfigTable.setStatus('current')
cvplsLdpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"))
if mibBuilder.loadTexts: cvplsLdpConfigEntry.setStatus('current')
cvplsLdpConfigMacAddrWithdraw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvplsLdpConfigMacAddrWithdraw.setStatus('current')
cvplsLdpPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvplsLdpPwBindTable.setStatus('current')
cvplsLdpPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex"))
if mibBuilder.loadTexts: cvplsLdpPwBindEntry.setStatus('current')
cvplsLdpPwBindMacAddressLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvplsLdpPwBindMacAddressLimit.setStatus('current')
cvplsLdpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1))
cvplsLdpModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1, 1)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpModuleFullCompliance = cvplsLdpModuleFullCompliance.setStatus('current')
cvplsLdpModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1, 2)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpModuleReadOnlyCompliance = cvplsLdpModuleReadOnlyCompliance.setStatus('current')
cvplsLdpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 2))
cvplsLdpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 2, 1)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpConfigMacAddrWithdraw"), ("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpPwBindMacAddressLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpGroup = cvplsLdpGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-VPLS-LDP-MIB", PYSNMP_MODULE_ID=cvplsLdpMIB, cvplsLdpCompliances=cvplsLdpCompliances, cvplsLdpConfigEntry=cvplsLdpConfigEntry, cvplsLdpConfigMacAddrWithdraw=cvplsLdpConfigMacAddrWithdraw, cvplsLdpConfigTable=cvplsLdpConfigTable, cvplsLdpConformance=cvplsLdpConformance, cvplsLdpGroup=cvplsLdpGroup, cvplsLdpGroups=cvplsLdpGroups, cvplsLdpMIB=cvplsLdpMIB, cvplsLdpModuleFullCompliance=cvplsLdpModuleFullCompliance, cvplsLdpModuleReadOnlyCompliance=cvplsLdpModuleReadOnlyCompliance, cvplsLdpObjects=cvplsLdpObjects, cvplsLdpPwBindEntry=cvplsLdpPwBindEntry, cvplsLdpPwBindMacAddressLimit=cvplsLdpPwBindMacAddressLimit, cvplsLdpPwBindTable=cvplsLdpPwBindTable)
