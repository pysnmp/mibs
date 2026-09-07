#
# PySNMP MIB module CISCO-BGP-POLICY-ACCOUNTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-BGP-POLICY-ACCOUNTING-MIB
# Source digest sha256:f7a56dcd396d0c53a404bb04c57ec5f96969481ea7800e8c51d4dc07490d31a6
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoBgpPolAcctMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 148))
ciscoBgpPolAcctMIB.setRevisions(('2002-07-26 00:00', '1999-12-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setRevisionsDescriptions(('Added egress, packet and octet, counters for the BGP\n                policy accounting feature.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setLastUpdated('2002-07-26 00:00')
if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setDescription('BGP policy based accounting information')
ciscoBgpPolAcctMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 1))
cbpAcctTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cbpAcctTable.setStatus('current')
if mibBuilder.loadTexts: cbpAcctTable.setDescription('The cbpAcctTable provides statistics about ingress and egress \n         traffic on an interface. This data could be used for purposes \n         like billing.')
cbpAcctEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"))
if mibBuilder.loadTexts: cbpAcctEntry.setStatus('current')
if mibBuilder.loadTexts: cbpAcctEntry.setDescription("Each cbpAcctEntry provides statistics for traffic of interest\n        on an ingress and/or egress interfaces. The traffic of interest \n        may be used for purposes like billing, and is referred to from \n        here on in the MIB by the term 'traffic-type', which corresponds\n        to cbpAcctTrafficIndex. Traffic-types are configured by the user\n        on a per interface basis.\n        \n        The statistics include ingress packet counts, ingress octet\n        counts, egress packet counts and egress octet counts. Entries \n        are created when traffic-type is configured on an interface.\n        Entries are deleted automatically when the user \n        removes the corresponding traffic-type configuration from an\n        interface.")
cbpAcctTrafficIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctTrafficIndex.setStatus('current')
if mibBuilder.loadTexts: cbpAcctTrafficIndex.setDescription('An integer value greater than 0, that uniquely identifies\n        a traffic-type. The traffic-type has no intrinsic meaning.\n        It just means the traffic coming into an interface can be\n        differentiated into different types. It is up to the user to\n        give meaning to and configure the various traffic-types on an \n        interface.')
cbpAcctInPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctInPacketCount.setStatus('current')
if mibBuilder.loadTexts: cbpAcctInPacketCount.setDescription('The total number of packets received for a particular\n        traffic-type on an interface.')
cbpAcctInOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctInOctetCount.setStatus('current')
if mibBuilder.loadTexts: cbpAcctInOctetCount.setDescription('The total number of octets received for a particular\n        traffic-type on an interface.')
cbpAcctOutPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctOutPacketCount.setStatus('current')
if mibBuilder.loadTexts: cbpAcctOutPacketCount.setDescription('The total number of packets transmitted for a particular\n        traffic-type on an interface.')
cbpAcctOutOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctOutOctetCount.setStatus('current')
if mibBuilder.loadTexts: cbpAcctOutOctetCount.setDescription('The total number of octets transmitted for a particular\n        traffic-type on an interface.')
ciscoBgpPolAcctMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 3))
ciscoBgpPolAcctMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1))
ciscoBgpPolAcctMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2))
ciscoBgpPolAcctMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1, 1)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBgpPolAcctMIBCompliance = ciscoBgpPolAcctMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoBgpPolAcctMIBCompliance.setDescription('The compliance statement for entities which implement\n                this Cisco BGP-Policy Traffic Accounting MIB.')
ciscoBgpPolAcctMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1, 2)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTableGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBgpPolAcctMIBComplianceRev1 = ciscoBgpPolAcctMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoBgpPolAcctMIBComplianceRev1.setDescription('The compliance statement for entities which implement\n                this Cisco BGP-Policy Traffic Accounting MIB.')
cbpAcctTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2, 1)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInPacketCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInOctetCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbpAcctTableGroup = cbpAcctTableGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cbpAcctTableGroup.setDescription('A collection of objects providing customer traffic \n                related parameters.')
cbpAcctTableGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2, 2)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInPacketCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInOctetCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctOutPacketCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctOutOctetCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbpAcctTableGroupRev1 = cbpAcctTableGroupRev1.setStatus('current')
if mibBuilder.loadTexts: cbpAcctTableGroupRev1.setDescription('A collection of objects providing customer traffic \n                related parameters.')
mibBuilder.exportSymbols("CISCO-BGP-POLICY-ACCOUNTING-MIB", PYSNMP_MODULE_ID=ciscoBgpPolAcctMIB, cbpAcctEntry=cbpAcctEntry, cbpAcctInOctetCount=cbpAcctInOctetCount, cbpAcctInPacketCount=cbpAcctInPacketCount, cbpAcctOutOctetCount=cbpAcctOutOctetCount, cbpAcctOutPacketCount=cbpAcctOutPacketCount, cbpAcctTable=cbpAcctTable, cbpAcctTableGroup=cbpAcctTableGroup, cbpAcctTableGroupRev1=cbpAcctTableGroupRev1, cbpAcctTrafficIndex=cbpAcctTrafficIndex, ciscoBgpPolAcctMIB=ciscoBgpPolAcctMIB, ciscoBgpPolAcctMIBCompliance=ciscoBgpPolAcctMIBCompliance, ciscoBgpPolAcctMIBComplianceRev1=ciscoBgpPolAcctMIBComplianceRev1, ciscoBgpPolAcctMIBCompliances=ciscoBgpPolAcctMIBCompliances, ciscoBgpPolAcctMIBConformance=ciscoBgpPolAcctMIBConformance, ciscoBgpPolAcctMIBGroups=ciscoBgpPolAcctMIBGroups, ciscoBgpPolAcctMIBObjects=ciscoBgpPolAcctMIBObjects)
