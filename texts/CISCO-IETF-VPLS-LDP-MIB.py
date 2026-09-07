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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cvplsLdpMIB.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: cvplsLdpMIB.setLastUpdated('2007-11-22 12:00')
if mibBuilder.loadTexts: cvplsLdpMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cvplsLdpMIB.setContactInfo('Cisco Systems\n            Customer Service \n\n            Postal:  \n            170 W Tasman Drive \n            San Jose, CA  95134 \n            USA \n\n            Tel: +1 800 553-NETS \n\n            E-mail: cs-l2vpn@cisco.com')
if mibBuilder.loadTexts: cvplsLdpMIB.setDescription('This MIB module contains managed object definitions for\n        LDP signalled Virtual Private LAN Services as in\n        [L2VPN-VPLS-LDP]\n\n        This MIB module enables the use of any underlying Pseudo Wire\n        network.\n\n        This MIB is based on the following IETF document.\n\n        http://www1.tools.ietf.org/html/draft-nadeau-l2vpn-vpls-mib-03')
cvplsLdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 1))
cvplsLdpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2))
cvplsLdpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvplsLdpConfigTable.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpConfigTable.setDescription('This table specifies information for configuring\n        and monitoring LDP specific parameters for\n        Virtual Private Lan Services(VPLS).')
cvplsLdpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"))
if mibBuilder.loadTexts: cvplsLdpConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpConfigEntry.setDescription('A row in this table represents LDP specific information\n        for Virtual Private Lan Service(VPLS) in a packet network.\n        It is indexed by cvplsConfigIndex, which uniquely\n        identifies a single VPLS.\n\n        A row is automatically created when a VPLS service is\n        configured using LDP signalling.\n\n        None of the read-create objects values can be\n        changed when cvplsRowStatus is in the active(1)\n        state. Changes are allowed when the cvplsRowStatus\n        is in notInService(2) or notReady(3) states only.\n        If the operator need to change one of the values\n        for an active row the cvplsConfigRowStatus should be\n        first changed to notInService(2), the objects may\n        be changed now, and later to active(1) in order to\n        re-initiate the signaling process with the new\n        values in effect.')
cvplsLdpConfigMacAddrWithdraw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvplsLdpConfigMacAddrWithdraw.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpConfigMacAddrWithdraw.setDescription('This object specifies if MAC address withdrawl is\n        enabled in this service. If this object is true then\n        Mac address withdrawl Learning is enabled. If false,\n        then Mac Learning is disabled.')
cvplsLdpPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvplsLdpPwBindTable.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpPwBindTable.setDescription('This table provides LDP specific information for\n        an association between a VPLS service and the\n        corresponding Pseudo Wires. A service can have more\n        than one Pseudo Wire association. Pseudo Wires are\n        defined in the cpwTable.')
cvplsLdpPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex"))
if mibBuilder.loadTexts: cvplsLdpPwBindEntry.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpPwBindEntry.setDescription('Each row represents an association between a\n        VPLS instance and one or more Pseudo Wires\n        defined in the cpwTable. Each index is unique\n        in describing an entry in this table. However\n        both indexes are required to define the one\n        to many association of service to pseudowire.\n\n        An entry in this table is instantiated only when \n        LDP signalling is used to configure VPLS service.\n\n        Each entry in this table provides LDP specific\n        information for the VPlS represented by \n        cvplsConfigIndex.')
cvplsLdpPwBindMacAddressLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvplsLdpPwBindMacAddressLimit.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpPwBindMacAddressLimit.setDescription('The value of this object specifies the maximum number\n        of learned and static entries allowed in the\n        Forwarding database for this PW Binding. The value 0\n        means there is no limit for this PW Binding.')
cvplsLdpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1))
cvplsLdpModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1, 1)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpModuleFullCompliance = cvplsLdpModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpModuleFullCompliance.setDescription('Compliance requirement for implementations that\n        provide full support for CISCO-IETF-VPLS-LDP-MIB.\n        Such devices can then be monitored and configured using \n        this MIB module.')
cvplsLdpModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1, 2)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpModuleReadOnlyCompliance = cvplsLdpModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpModuleReadOnlyCompliance.setDescription('Compliance requirement for implementations that only\n        provide read-only support for CISCO-IETF-VPLS-LDP-MIB.\n        Such devices can then be monitored but cannot be\n        configured using this MIB modules.')
cvplsLdpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 2))
cvplsLdpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 2, 1)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpConfigMacAddrWithdraw"), ("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpPwBindMacAddressLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpGroup = cvplsLdpGroup.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpGroup.setDescription('The group of objects supporting\n        management of L2VPN VPLS services using LDP.')
mibBuilder.exportSymbols("CISCO-IETF-VPLS-LDP-MIB", PYSNMP_MODULE_ID=cvplsLdpMIB, cvplsLdpCompliances=cvplsLdpCompliances, cvplsLdpConfigEntry=cvplsLdpConfigEntry, cvplsLdpConfigMacAddrWithdraw=cvplsLdpConfigMacAddrWithdraw, cvplsLdpConfigTable=cvplsLdpConfigTable, cvplsLdpConformance=cvplsLdpConformance, cvplsLdpGroup=cvplsLdpGroup, cvplsLdpGroups=cvplsLdpGroups, cvplsLdpMIB=cvplsLdpMIB, cvplsLdpModuleFullCompliance=cvplsLdpModuleFullCompliance, cvplsLdpModuleReadOnlyCompliance=cvplsLdpModuleReadOnlyCompliance, cvplsLdpObjects=cvplsLdpObjects, cvplsLdpPwBindEntry=cvplsLdpPwBindEntry, cvplsLdpPwBindMacAddressLimit=cvplsLdpPwBindMacAddressLimit, cvplsLdpPwBindTable=cvplsLdpPwBindTable)
