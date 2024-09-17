#
# PySNMP MIB module AT-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-IP-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 09:56:51 2024
# On host fv-az1427-100 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, TimeTicks, ModuleIdentity, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Gauge32, NotificationType, iso, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Gauge32", "NotificationType", "iso", "Counter64", "Integer32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
atIpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602))
atIpMib.setRevisions(('2010-06-14 05:09', '2008-11-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atIpMib.setRevisionsDescriptions(('MIB revision history dates in descriptions updated.', 'Initial revision.',))
if mibBuilder.loadTexts: atIpMib.setLastUpdated('201006140509Z')
if mibBuilder.loadTexts: atIpMib.setOrganization('Allied Telesis Labs New Zealand')
if mibBuilder.loadTexts: atIpMib.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atIpMib.setDescription('The IP MIB - for AT specific IP management.')
class AtIpAddressAssignmentType(TextualConvention, Integer32):
    description = 'The IP address assignment type being applied to the interface.\n                notSet(0) indicates that the IP address assignment type has\n                not yet been configured. This value can only ever be read.\n                primary(1) indicates that the address is a primary IP address\n                (only one primary address is allowed per interface).\n                secondary(2) indicates that the address is a secondary IP\n                address (any number of secondary IP addresses may be applied\n                to each interface).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notSet", 0), ("primary", 1), ("secondary", 2))

atIpAddressTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1), )
if mibBuilder.loadTexts: atIpAddressTable.setStatus('current')
if mibBuilder.loadTexts: atIpAddressTable.setDescription('A table containing mappings between primary/secondary IP\n                addresses, and the interfaces they are assigned to.')
atIpAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1), ).setIndexNames((0, "AT-IP-MIB", "atIpAddressAddrType"), (0, "AT-IP-MIB", "atIpAddressAddr"))
if mibBuilder.loadTexts: atIpAddressEntry.setStatus('current')
if mibBuilder.loadTexts: atIpAddressEntry.setDescription('An address mapping for a particular interface.')
atIpAddressAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: atIpAddressAddrType.setStatus('current')
if mibBuilder.loadTexts: atIpAddressAddrType.setDescription('An indication of the IP version of atIpAddressAddr.')
atIpAddressAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: atIpAddressAddr.setStatus('current')
if mibBuilder.loadTexts: atIpAddressAddr.setDescription("The IP address to which this entry's addressing information\n                pertains. The address type of this object is specified in\n                atIpAddressAddrType.")
atIpAddressPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressPrefixLen.setStatus('current')
if mibBuilder.loadTexts: atIpAddressPrefixLen.setDescription('The prefix length of the IP address represented by this entry.')
atIpAddressLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressLabel.setStatus('current')
if mibBuilder.loadTexts: atIpAddressLabel.setDescription('A name assigned to the IP address represented by this entry.')
atIpAddressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 5), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressIfIndex.setStatus('current')
if mibBuilder.loadTexts: atIpAddressIfIndex.setDescription("The index value that uniquely identifies the interface to\n                which this entry is applicable.  The interface identified by\n                a particular value of this index is the same interface as\n                identified by the same value of the IF-MIB's ifIndex.")
atIpAddressAssignmentType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 6), AtIpAddressAssignmentType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressAssignmentType.setStatus('current')
if mibBuilder.loadTexts: atIpAddressAssignmentType.setDescription('The IP address assignment type for this entry (primary or\n                secondary).')
atIpAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressRowStatus.setStatus('current')
if mibBuilder.loadTexts: atIpAddressRowStatus.setDescription('The current status of the IP address entry. The following\n                values may be returned when reading this object:\n\n                active (1)        - The IP address is currently mapped to\n                                    an interface and is valid.\n                notReady (3)      - The IP address is currently partially\n                                    configured and is not mapped to an\n                                    interface.\n\n                The following values may be written to this object:\n\n                active (1)        - An attempt will be made to map the IP\n                                    address to the configured interface.\n                createAndWait (5) - An attempt will be made to create a new\n                                    IP address entry.\n                destroy (6)       - The IP address setting will be removed\n                                    from the device.\n\n                An entry cannot be made active until its atIpAddressPrefixLen,\n                atIpAddressIfIndex and atIpAddressAssignmentType objects have\n                been set to valid values.')
mibBuilder.exportSymbols("AT-IP-MIB", atIpAddressAssignmentType=atIpAddressAssignmentType, PYSNMP_MODULE_ID=atIpMib, atIpAddressTable=atIpAddressTable, atIpAddressAddr=atIpAddressAddr, AtIpAddressAssignmentType=AtIpAddressAssignmentType, atIpAddressAddrType=atIpAddressAddrType, atIpAddressPrefixLen=atIpAddressPrefixLen, atIpAddressLabel=atIpAddressLabel, atIpMib=atIpMib, atIpAddressRowStatus=atIpAddressRowStatus, atIpAddressEntry=atIpAddressEntry, atIpAddressIfIndex=atIpAddressIfIndex)
