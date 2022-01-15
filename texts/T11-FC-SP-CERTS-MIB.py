#
# PySNMP MIB module T11-FC-SP-CERTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/T11-FC-SP-CERTS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 14:59:54 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fcmInstanceIndex, = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmInstanceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, MibIdentifier, Bits, mib_2, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, ObjectIdentity, Counter32, TimeTicks, IpAddress, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "Bits", "mib-2", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "ObjectIdentity", "Counter32", "TimeTicks", "IpAddress", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
t11FcSpAuEntityName, = mibBuilder.importSymbols("T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuEntityName")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
t11FcSpCertsMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 1))
t11FcSpCertsMIB.setRevisions(('2007-02-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: t11FcSpCertsMIB.setRevisionsDescriptions(('Initial version of this MIB module, published as RFCyyyy.',))
if mibBuilder.loadTexts: t11FcSpCertsMIB.setLastUpdated('200702190000Z')
if mibBuilder.loadTexts: t11FcSpCertsMIB.setOrganization('T11')
if mibBuilder.loadTexts: t11FcSpCertsMIB.setContactInfo('     Claudio DeSanti\n                  Cisco Systems, Inc.\n                  170 West Tasman Drive\n                  San Jose, CA 95134 USA\n                  EMail: cds@cisco.com\n\n                  Keith McCloghrie\n                  Cisco Systems, Inc.\n                  170 West Tasman Drive\n                  San Jose, CA 95134 USA\n                  Email: kzm@cisco.com')
if mibBuilder.loadTexts: t11FcSpCertsMIB.setDescription("This MIB module defines management information specific to\n           the use of certificates in conjunction with Fibre Channel's\n           FC-SP specification.\n\n           Since FC-SP leverages a subset of IPsec and IKEv2 (see RFC\n           4595), a subset of the management information defined for\n           the use of certificates with IPsec/IKEv2 is also applicable\n           to FC-SP.  Thus, this MIB module leverages RFC wwww and\n           RFC xxxx for the management of certificates, CAs and CRLs.\n-- RFC Editor: replace wwww with actual RFC number for\n-- [IPSP-IPSEC-ACTION], and replace xxxx with actual RFC number for\n-- [IPSP-IKE-ACTION] & remove this note\n\n           Specifically, the information defined in this MIB module\n           consists of a pointer into the IPsec/IKEv2 MIB modules,\n           plus minimal additional item(s) of information which are\n           considered to be important in a Fibre Channel environment.\n\n           Copyright (C) The IETF Trust (2007).  This version\n           of this MIB module is part of RFC yyyy;  see the RFC\n           itself for full legal notices.")
t11FcSpCertsMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 1))
t11FcSpCertsMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 2))
t11FcSpCertsTable = MibTable((1, 3, 6, 1, 2, 1, 1, 1, 1), )
if mibBuilder.loadTexts: t11FcSpCertsTable.setStatus('current')
if mibBuilder.loadTexts: t11FcSpCertsTable.setDescription("A table containing information on the use of certificates\n           in FC-SP, including (but not limited to) the use of\n           certificates with the Fibre Channel Certificate\n           Authentication Protocol (FCAP) defined by FC-SP, or with\n           FC-SP's use of IKEv2.")
t11FcSpCertsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "T11-FC-SP-AUTHENTICATION-MIB", "t11FcSpAuEntityName"), (0, "T11-FC-SP-CERTS-MIB", "t11FcSpCertFabricIndex"), (0, "T11-FC-SP-CERTS-MIB", "t11FcSpCertIndex"))
if mibBuilder.loadTexts: t11FcSpCertsEntry.setStatus('current')
if mibBuilder.loadTexts: t11FcSpCertsEntry.setDescription('Each entry contains information related to one certificate\n           for use by the FC-SP Authentication entity identified by\n           t11FcSpAuEntityName, on a particular Fabric, which is managed\n           as part of the Fibre Channel management instance identified\n           by fcmInstanceIndex.')
t11FcSpCertFabricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 1), T11FabricIndex())
if mibBuilder.loadTexts: t11FcSpCertFabricIndex.setStatus('current')
if mibBuilder.loadTexts: t11FcSpCertFabricIndex.setDescription('An index value which uniquely identifies a particular\n           Fabric where the certificate is available for use.')
t11FcSpCertIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: t11FcSpCertIndex.setStatus('current')
if mibBuilder.loadTexts: t11FcSpCertIndex.setDescription('This object distinguishes between the multiple certificates\n           available for use with FC-SP on a particular Fabric.')
t11FcSpCertPointer = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpCertPointer.setStatus('current')
if mibBuilder.loadTexts: t11FcSpCertPointer.setDescription("This object contains the 'name' of a row in the\n           ipsaCredentialTable, i.e., it points to the certificate which\n           is represented by the row of the ipsaCredentialTable for\n           which the value of ipsaCredName has the same value as the\n           value of this object.  Further information about the\n           certificate is available in that row.\n\n           If and when there is no row in the psaCredentialTable for\n           this certificate, the value of this object is the zero-length\n           string.")
t11FcSpCertUsage = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ownDefaultCert", 2), ("ownCert", 3), ("rootCert", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpCertUsage.setStatus('current')
if mibBuilder.loadTexts: t11FcSpCertUsage.setDescription('This object identifies how this certificate can be used:\n\n              other -- none of the below;\n\n              ownDefaultCert -- the certificate which the local entity\n                       uses as its default certificate; the local entity\n                       has at most one default certificate;\n\n              ownCert  -- a certificate which the local entity can use\n                       for itself, but which is not its default\n                       certificate;\n\n              rootCert -- a root certificate.\n            ')
t11FcSpCertMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 2, 1))
t11FcSpCertMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 2, 2))
t11FcSpCertMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 1, 2, 1, 1)).setObjects(("T11-FC-SP-CERTS-MIB", "t11FcSpCertInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpCertMIBCompliance = t11FcSpCertMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: t11FcSpCertMIBCompliance.setDescription('The compliance statement for entities which use\n           certificates with FC-SP.')
t11FcSpCertInfoGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 1, 2, 2, 1)).setObjects(("T11-FC-SP-CERTS-MIB", "t11FcSpCertPointer"), ("T11-FC-SP-CERTS-MIB", "t11FcSpCertUsage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpCertInfoGroup = t11FcSpCertInfoGroup.setStatus('current')
if mibBuilder.loadTexts: t11FcSpCertInfoGroup.setDescription('A collection of objects containing information\n           related to certificates available for use with FC-SP.')
mibBuilder.exportSymbols("T11-FC-SP-CERTS-MIB", t11FcSpCertMIBGroups=t11FcSpCertMIBGroups, t11FcSpCertInfoGroup=t11FcSpCertInfoGroup, t11FcSpCertsMIBConformance=t11FcSpCertsMIBConformance, t11FcSpCertIndex=t11FcSpCertIndex, t11FcSpCertMIBCompliance=t11FcSpCertMIBCompliance, t11FcSpCertMIBCompliances=t11FcSpCertMIBCompliances, t11FcSpCertsMIBObjects=t11FcSpCertsMIBObjects, t11FcSpCertsEntry=t11FcSpCertsEntry, t11FcSpCertsMIB=t11FcSpCertsMIB, t11FcSpCertFabricIndex=t11FcSpCertFabricIndex, t11FcSpCertsTable=t11FcSpCertsTable, PYSNMP_MODULE_ID=t11FcSpCertsMIB, t11FcSpCertUsage=t11FcSpCertUsage, t11FcSpCertPointer=t11FcSpCertPointer)
