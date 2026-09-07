#
# PySNMP MIB module CISCO-WAN-ATM-CUG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-ATM-CUG-MIB
# Source digest sha256:4edf02d2167e71e9b384d1c508275add5916102c8da193295867a255dbab59aa
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
AtmAddr, = mibBuilder.importSymbols("ATM-TC-MIB", "AtmAddr")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoWanAtmCugMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 99999))
ciscoWanAtmCugMIB.setRevisions(('2002-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanAtmCugMIB.setRevisionsDescriptions(('Initial version of the MIB.',))
if mibBuilder.loadTexts: ciscoWanAtmCugMIB.setLastUpdated('2002-03-22 00:00')
if mibBuilder.loadTexts: ciscoWanAtmCugMIB.setOrganization('Cisco System Inc.')
if mibBuilder.loadTexts: ciscoWanAtmCugMIB.setContactInfo('           Cisco Systems\n                    Customer Service\n\n                    Postal: 170 West Tasman Drive,\n                            San Jose CA 95134-1706.\n                            USA\n\n                    Tel: +1 800 553-NETS\n\n                    E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanAtmCugMIB.setDescription("This MIB module is intended for the management of  \n         'Closed User Group(CUG)' in Cisco ATM switches.  \n\n         This MIB definition is based upon 'Closed User Group'\n         recommended by International Telecommunication Union(ITU). \n\n         The CUG supplementary service enables users to form groups,\n         to and from which access is restricted. A specific user may\n         be member of one or more closed user groups. Members of a\n         specific closed user group can communicate among themselves\n         but not, in general, with users outside the group. Specific    \n         CUG members can have additional capabilities that allow \n         them to originate calls to destinations outside the group,\n         and/or to receive calls from outside the group. Specific\n         CUG members can have additional restrictions that prevent\n         them from originating calls to other members of the CUG,\n         or from receiving calls from other members of the CUG.\n\n         ITU-T Q.2955.1 Stage 3 description for community of interest\n         supplementary services using B-ISDN Digital Subscriber\n         Signalling System No.2(DSS 2): Closed User Group(CUG).")
cwaCugMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 0))
cwaCugMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1))
cwaCug = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1))
cwaAddressCug = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2))
class CiscoAtmAddressType(TextualConvention, Integer32):
    description = 'The type of an ATM Address. \n\n         The value e164(3) indicates the address format \n         is that of ITU-T defined address format.\n\n\t The value nsap(8) indicates the address format \n         is that of ATM private network address or ATM \n         end-point identifiers.\n\n         The CiscoAtmAddressType textual convention SHOULD\n         NOT be subtyped in object type definitions to support\n         future extensions. It MAY be subtyped in compliance \n         statements in order to require only a subset of \n         these address types for a compliant implementation.\n\n         Note that the enumerated values of this TC are\n         aligned with AddressFamilyNumbers from \n         IANA-ADDRESS-FAMILY-NUMBERS-MIB.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 8))
    namedValues = NamedValues(("e164", 3), ("nsap", 8))

class CiscoAtmAddressLength(TextualConvention, Integer32):
    description = 'The length (in bits) of an ATM Address.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 160)

class CiscoAtmInterlockCode(TextualConvention, OctetString):
    reference = 'ATM Forum, Closed User Group, Section 3'
    description = "A Closed User Group(CUG) Interlock Code. Each\n         'Interlock Code' uniquely identifies a Closed\n         User Group in the network. This is a\n         'PNNI Interlock Code', it contains a 20-octet\n         ATM End Station Address(AESA) and a 4-octet Suffix.\n         "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(24, 24)
    fixedLength = 24

cwaCugTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cwaCugTable.setStatus('current')
if mibBuilder.loadTexts: cwaCugTable.setDescription('This table contains a sequence of CUGs for each\n         ATM address.')
cwaCugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-WAN-ATM-CUG-MIB", "cwaAtmAddress"), (0, "CISCO-WAN-ATM-CUG-MIB", "cwaAddressLength"), (0, "CISCO-WAN-ATM-CUG-MIB", "cwaCugIndex"))
if mibBuilder.loadTexts: cwaCugEntry.setStatus('current')
if mibBuilder.loadTexts: cwaCugEntry.setDescription('The entry represents one CUG for an ATM address.')
cwaAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 1), AtmAddr()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cwaAtmAddress.setStatus('current')
if mibBuilder.loadTexts: cwaAtmAddress.setDescription('A provisioned ATM address on the managed system.')
cwaAddressLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 2), CiscoAtmAddressLength()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cwaAddressLength.setStatus('current')
if mibBuilder.loadTexts: cwaAddressLength.setDescription("This is the length (in bits) of the 'cwtAtmAddress'. \n         ")
cwaCugIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cwaCugIndex.setReference('ITU-T Specification Q.2955.1 section 1.3.3')
if mibBuilder.loadTexts: cwaCugIndex.setStatus('current')
if mibBuilder.loadTexts: cwaCugIndex.setDescription("The CUG index is a parameter used by the calling\n         user to select a particular CUG when originating\n         a call. The index is also used by the network to\n         indicate to the called user the CUG from which \n         an incoming call has originated. This index has\n         only local significance.\n\n         Each 'cwaCugIndex' assigned to an ATM address must be\n         unique for this ATM address. For each 'cwaCugIndex'\n         must have one corresponding cwaInterLockCode\n         assigned.")
cwaAddressPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 4), CiscoAtmAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaAddressPlan.setStatus('current')
if mibBuilder.loadTexts: cwaAddressPlan.setDescription('This is the type of the ATM address associated\n         with this entry.')
cwaInterlockCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 5), CiscoAtmInterlockCode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaInterlockCode.setReference('ATM Forum, Closed User Group, Section 3')
if mibBuilder.loadTexts: cwaInterlockCode.setStatus('current')
if mibBuilder.loadTexts: cwaInterlockCode.setDescription("This is the 'Closed User Group(CUG) Interlock Code'\n         associated with this entry.")
cwaCallsBarred = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("incoming", 2), ("outgoing", 3))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaCallsBarred.setReference('ITU-T Specification Q.2955.1 Sections 1.3.9 and 1.3.13')
if mibBuilder.loadTexts: cwaCallsBarred.setStatus('current')
if mibBuilder.loadTexts: cwaCallsBarred.setDescription('This variable indicates if this member can receive calls \n         from or make calls to other members of the same CUG.\n\n         When this variable is set to none(1), it means this\n         CUG member can receive calls from and make calls to \n         other members in the same CUG.\n\n         When this variable is set to incoming(2), it means this\n         member cannot receive incoming calls from other members\n         in the same CUG.\n\n         When this variable is set to outgoing(3), it means this\n         member cannot make calls to other members in the same CUG.\n         ')
cwaCugRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaCugRowStatus.setStatus('current')
if mibBuilder.loadTexts: cwaCugRowStatus.setDescription("The row status of each entry in this table.\n         \n         Once the 'cwaInterlockCode' is created, it cannot be\n         modified. If the management station wants to\n         assign a different Interlock Code to the same\n         'cwaCugIndex', the management station must remove\n         the current entry and then add a new entry with\n         the same 'cwaCugIndex' and a different 'cwaInterlockCode.")
cwaAddressCugTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cwaAddressCugTable.setReference('ITU-T Specification Q.2955.1 Section 1.3')
if mibBuilder.loadTexts: cwaAddressCugTable.setStatus('current')
if mibBuilder.loadTexts: cwaAddressCugTable.setDescription('A table of CUG parameters associated with\n         each provisioned ATM address.')
cwaAddressCugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-WAN-ATM-CUG-MIB", "cwaAtmAddress"), (0, "CISCO-WAN-ATM-CUG-MIB", "cwaAddressLength"))
if mibBuilder.loadTexts: cwaAddressCugEntry.setStatus('current')
if mibBuilder.loadTexts: cwaAddressCugEntry.setDescription("The managed system will automatically create\n         an entry in this table when the first CUG \n         is created for the same ATM address in  \n         'cwaCugTable'.\n\n         A entry in this table is automatically \n         destroyed by the managed system when all \n         CUGs of the same ATM address are destroyed\n\t in the 'cwaCugTable'.")
cwaCugAtmAddressPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 1), CiscoAtmAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaCugAtmAddressPlan.setStatus('current')
if mibBuilder.loadTexts: cwaCugAtmAddressPlan.setDescription('This is the type of the ATM address associated\n         with this entry.')
cwaIncomingAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notAllowed", 1), ("allowed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaIncomingAccess.setReference('ITU-T Specification Q.2955.1 section 1.3.8')
if mibBuilder.loadTexts: cwaIncomingAccess.setStatus('current')
if mibBuilder.loadTexts: cwaIncomingAccess.setDescription("This variable decides whether 'incoming access' \n         is allowed for a CUG user.\n         \n         the 'incoming access' allows a CUG user to receive \n         calls from all other non-CUG users and also from those\n         other CUG user that allow 'outgoing access'.\n\n         When the value is set to notAllowed(1), the  \n         'incoming access' is not allowed. \n\n         When the value is set to allowed(2), the 'incoming  \n         access' is allowed.\n\n         When this entry is created, this variable has a \n         value of notAllowed(1).")
cwaOutgoingAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notAllowed", 1), ("allowedPerCall", 2), ("allowedPermanently", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaOutgoingAccess.setReference('ITU-T Specification Q.2955.1 section 1.3.9')
if mibBuilder.loadTexts: cwaOutgoingAccess.setStatus('current')
if mibBuilder.loadTexts: cwaOutgoingAccess.setDescription("This variable decides whether 'outgoing access' \n         is allowed for a CUG user. \n\n         The 'outgoing access' allows a member of a CUG to make  \n         calls to other non-CUG members and also to those\n         other CUG members that allow 'incoming access'.\n\n         When the value is set to notAllowed(1), the 'outgoinging \n         access' is not allowed. \n          \n         When the value is set to allowedPerCall(2), the \n         'outgoing access' is granted on a per call basis. This\n         means for each call, the 'outgoing access' request must\n         be part of the call SETUP message. \n\n         When the value is set to allowedPermanently(3),  \n         the 'outgoing access' is allowed for all calls. \n         When this entry is created by the managed \n         system, this variable has a value of notAllowed(1).")
cwaPreferentialCug = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99999, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwaPreferentialCug.setReference('ITU-T Specification Q.2955.1 section 1.3.14')
if mibBuilder.loadTexts: cwaPreferentialCug.setStatus('current')
if mibBuilder.loadTexts: cwaPreferentialCug.setDescription("The CUG index of the 'preferential CUG' for this address.\n         There can be only one 'preferential CUG' for an address.\n         \n         A CUG user subscribing to 'preferential CUG' nominates a\n         CUG index which the network uses as a default to identify\n         the required CUG in the absence of any CUG information\n         in the outgoing call request. \n\n         A value of zero means the address does not have a \n         preferential CUG. The value of this variable must \n         correspond to a 'cwaCugIndex' of an entry in the  \n         'cwaCugTable'. When an entry is created by the managed \n         system, this variable has a value of 0. \n\n         When selecting a 'preferential' CUG in the address's CUGs,\n         the corresponding CUG must allow outgoing calls.  \n         This means 'cwaCallsBarred'(Outgoing Calls Barred) \n\t must not have a value of outgoing(2) for the corresponding\n\t CUG.")
ciscoWanAtmCugMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3))
ciscoWanAtmCugMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 1))
ciscoWanAtmCugMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2))
ciscoWanAtmCugMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 1, 1)).setObjects(("CISCO-WAN-ATM-CUG-MIB", "ciscoWanAtmCugGroup"), ("CISCO-WAN-ATM-CUG-MIB", "ciscoWanAtmAddressCugGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmCugMIBCompliance = ciscoWanAtmCugMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAtmCugMIBCompliance.setDescription('The compliance statement for SNMPv2 entities which\n         implement Closed User Groups(CUG).')
ciscoWanAtmCugGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2, 1)).setObjects(("CISCO-WAN-ATM-CUG-MIB", "cwaAddressPlan"), ("CISCO-WAN-ATM-CUG-MIB", "cwaInterlockCode"), ("CISCO-WAN-ATM-CUG-MIB", "cwaCallsBarred"), ("CISCO-WAN-ATM-CUG-MIB", "cwaCugRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmCugGroup = ciscoWanAtmCugGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAtmCugGroup.setDescription('This group contains the CUGs for each ATM\n         address on the managed system.')
ciscoWanAtmAddressCugGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99999, 3, 2, 2)).setObjects(("CISCO-WAN-ATM-CUG-MIB", "cwaCugAtmAddressPlan"), ("CISCO-WAN-ATM-CUG-MIB", "cwaIncomingAccess"), ("CISCO-WAN-ATM-CUG-MIB", "cwaOutgoingAccess"), ("CISCO-WAN-ATM-CUG-MIB", "cwaPreferentialCug"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmAddressCugGroup = ciscoWanAtmAddressCugGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAtmAddressCugGroup.setDescription('This group contains objects for the CUG for each \n         ATM address on the managed system.')
mibBuilder.exportSymbols("CISCO-WAN-ATM-CUG-MIB", CiscoAtmAddressLength=CiscoAtmAddressLength, CiscoAtmAddressType=CiscoAtmAddressType, CiscoAtmInterlockCode=CiscoAtmInterlockCode, PYSNMP_MODULE_ID=ciscoWanAtmCugMIB, ciscoWanAtmAddressCugGroup=ciscoWanAtmAddressCugGroup, ciscoWanAtmCugGroup=ciscoWanAtmCugGroup, ciscoWanAtmCugMIB=ciscoWanAtmCugMIB, ciscoWanAtmCugMIBCompliance=ciscoWanAtmCugMIBCompliance, ciscoWanAtmCugMIBCompliances=ciscoWanAtmCugMIBCompliances, ciscoWanAtmCugMIBConformance=ciscoWanAtmCugMIBConformance, ciscoWanAtmCugMIBGroups=ciscoWanAtmCugMIBGroups, cwaAddressCug=cwaAddressCug, cwaAddressCugEntry=cwaAddressCugEntry, cwaAddressCugTable=cwaAddressCugTable, cwaAddressLength=cwaAddressLength, cwaAddressPlan=cwaAddressPlan, cwaAtmAddress=cwaAtmAddress, cwaCallsBarred=cwaCallsBarred, cwaCug=cwaCug, cwaCugAtmAddressPlan=cwaCugAtmAddressPlan, cwaCugEntry=cwaCugEntry, cwaCugIndex=cwaCugIndex, cwaCugMIBNotifications=cwaCugMIBNotifications, cwaCugMIBObjects=cwaCugMIBObjects, cwaCugRowStatus=cwaCugRowStatus, cwaCugTable=cwaCugTable, cwaIncomingAccess=cwaIncomingAccess, cwaInterlockCode=cwaInterlockCode, cwaOutgoingAccess=cwaOutgoingAccess, cwaPreferentialCug=cwaPreferentialCug)
