#
# PySNMP MIB module CLAB-TOPO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/CLAB-TOPO-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:08:23 2022
# On host fv-az74-933 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
clabCommonMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabCommonMibs")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Gauge32, NotificationType, Unsigned32, iso, ModuleIdentity, Counter64, Counter32, ObjectIdentity, Bits, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "NotificationType", "Unsigned32", "iso", "ModuleIdentity", "Counter64", "Counter32", "ObjectIdentity", "Bits", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
clabTopoMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 4, 2))
clabTopoMib.setRevisions(('2017-06-15 00:00', '2009-01-21 00:00', '2006-12-07 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: clabTopoMib.setRevisionsDescriptions(('Revised Version includes ECN\n         CLAB-TOPO-MIB-N-17.0161-1 to add Apache License.', 'Revised Version includes ECNs\n         OSSIv3.0-N-08.0651-3\n         OSSIv3.0-N-08.0700-4\n         and published as I08', 'Initial version, published as part of the CableLabs\n        OSSIv3.0 specification CM-SP-OSSIv3.0-I01-061207\n        Copyright 1999-2009 Cable Television Laboratories, Inc.\n        All rights reserved.',))
if mibBuilder.loadTexts: clabTopoMib.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: clabTopoMib.setOrganization('Cable Television Laboratories, Inc.')
if mibBuilder.loadTexts: clabTopoMib.setContactInfo('\n         Postal: Cable Television Laboratories, Inc.\n         858 Coal Creek Circle\n         Louisville, Colorado 80027-9750\n         U.S.A.\n         Phone: +1 303-661-9100\n         Fax:   +1 303-661-9199\n         E-mail: mibs@cablelabs.com')
if mibBuilder.loadTexts: clabTopoMib.setDescription("Licensed under the Apache License, Version 2.0 (the 'License');\n         you may not use this file except in compliance with the License.\n         You may obtain a copy of the License at:\n \n             http://www.apache.org/licenses/LICENSE-2.0\n \n         Unless required by applicable law or agreed to in writing, software\n         distributed under the License is distributed on an 'AS IS' BASIS,\n         WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or \n         implied.\n\n         See the License for the specific language governing permissions and\n         limitations under the License.\n\n         This MIB module contains the management objects for the\n         management of fiber nodes in the Cable plant.\n         Copyright 2006-2017 Cable Television Laboratories, Inc.\n         All rights reserved.")
class NodeName(TextualConvention, OctetString):
    reference = 'RFC 3411.'
    description = 'This data type is a human readable string that represents\n        the name of a fiber node. Internationalization is supported\n        by conforming to the SNMP textual convention SnmpAdminString.\n        The US-ASCII control characters (0x00  0x1F), the DEL\n        Character (0x7F), and the double-quote mark (0x22) are \n        prohibited within the syntax of this data type.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

clabTopoMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1))
clabTopoFiberNodeCfgTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1), )
if mibBuilder.loadTexts: clabTopoFiberNodeCfgTable.setStatus('current')
if mibBuilder.loadTexts: clabTopoFiberNodeCfgTable.setDescription('This object defines the cable HFC plant Fiber Nodes\n        known at a CMTS.\n        This object supports the creation and deletion of multiple\n        instances.')
clabTopoFiberNodeCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1), ).setIndexNames((0, "CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeName"))
if mibBuilder.loadTexts: clabTopoFiberNodeCfgEntry.setStatus('current')
if mibBuilder.loadTexts: clabTopoFiberNodeCfgEntry.setDescription('The conceptual row of clabTopoFiberNodeCfg.\n         The CMTS persists all instances of FiberNodeCfg\n         across reinitializations.')
clabTopoFiberNodeCfgNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 1), NodeName().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeName.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804, RF Topology \n         Configuration section.')
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeName.setStatus('current')
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeName.setDescription('This key represents a human-readable name for a fiber\n        node.')
clabTopoFiberNodeCfgNodeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 2), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeDescr.setStatus('current')
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeDescr.setDescription('Administratively configured human-readable description\n        of the fiber node')
clabTopoFiberNodeCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: clabTopoFiberNodeCfgRowStatus.setStatus('current')
if mibBuilder.loadTexts: clabTopoFiberNodeCfgRowStatus.setDescription('The status of this instance.')
clabTopoChFnCfgTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2), )
if mibBuilder.loadTexts: clabTopoChFnCfgTable.setStatus('current')
if mibBuilder.loadTexts: clabTopoChFnCfgTable.setDescription("This object defines the RF topology by defining the\n        connectivity of a CMTS's downstream and upstream channels\n        to the fiber nodes. Each instance of this object\n        describes connectivity of one downstream or upstream\n        channel with a single fiber node.\n        This object supports the creation and deletion of multiple\n        instances.")
clabTopoChFnCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1), ).setIndexNames((0, "CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeName"), (0, "CLAB-TOPO-MIB", "clabTopoChFnCfgChIfIndex"))
if mibBuilder.loadTexts: clabTopoChFnCfgEntry.setStatus('current')
if mibBuilder.loadTexts: clabTopoChFnCfgEntry.setDescription('The conceptual row of clabTopoChFnCfg.\n          The CMTS persists all instances of ChFnCfg\n          across reinitializations.')
clabTopoChFnCfgChIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: clabTopoChFnCfgChIfIndex.setStatus('current')
if mibBuilder.loadTexts: clabTopoChFnCfgChIfIndex.setDescription('This key represents the interface index of an upstream\n        or downstream channel associated with this fiber\n        node. In the upstream direction, only ifIndices\n        docsCableUpstream channels are reflected.')
clabTopoChFnCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: clabTopoChFnCfgRowStatus.setStatus('current')
if mibBuilder.loadTexts: clabTopoChFnCfgRowStatus.setDescription('The status of this instance.')
clabTopoMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2))
clabTopoMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 1))
clabTopoMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 2))
clabTopoCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 1, 1)).setObjects(("CLAB-TOPO-MIB", "clabTopoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clabTopoCompliance = clabTopoCompliance.setStatus('current')
if mibBuilder.loadTexts: clabTopoCompliance.setDescription('The compliance statement for devices that implement the\n         CableLabs Topology MIB.')
clabTopoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 2, 1)).setObjects(("CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeDescr"), ("CLAB-TOPO-MIB", "clabTopoFiberNodeCfgRowStatus"), ("CLAB-TOPO-MIB", "clabTopoChFnCfgRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clabTopoGroup = clabTopoGroup.setStatus('current')
if mibBuilder.loadTexts: clabTopoGroup.setDescription('Group of objects implemented in the CMTS.')
mibBuilder.exportSymbols("CLAB-TOPO-MIB", clabTopoChFnCfgTable=clabTopoChFnCfgTable, clabTopoFiberNodeCfgNodeName=clabTopoFiberNodeCfgNodeName, clabTopoChFnCfgChIfIndex=clabTopoChFnCfgChIfIndex, clabTopoFiberNodeCfgRowStatus=clabTopoFiberNodeCfgRowStatus, clabTopoMibConformance=clabTopoMibConformance, clabTopoMibGroups=clabTopoMibGroups, clabTopoMib=clabTopoMib, clabTopoFiberNodeCfgTable=clabTopoFiberNodeCfgTable, clabTopoChFnCfgEntry=clabTopoChFnCfgEntry, clabTopoFiberNodeCfgEntry=clabTopoFiberNodeCfgEntry, clabTopoGroup=clabTopoGroup, clabTopoChFnCfgRowStatus=clabTopoChFnCfgRowStatus, NodeName=NodeName, clabTopoCompliance=clabTopoCompliance, clabTopoFiberNodeCfgNodeDescr=clabTopoFiberNodeCfgNodeDescr, clabTopoMibObjects=clabTopoMibObjects, clabTopoMibCompliances=clabTopoMibCompliances, PYSNMP_MODULE_ID=clabTopoMib)
