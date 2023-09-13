#
# PySNMP MIB module ENTERASYS-MIB-NAMES (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/ENTERASYS-MIB-NAMES
# Produced by pysmi-1.1.8 at Wed Sep 13 14:56:25 2023
# On host fv-az484-871 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, NotificationType, Unsigned32, enterprises, Integer32, Counter32, Counter64, Gauge32, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "NotificationType", "Unsigned32", "enterprises", "Integer32", "Counter32", "Counter64", "Gauge32", "IpAddress", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysModuleName = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 1))
etsysModuleName.setRevisions(('2003-11-06 15:15', '2003-10-23 17:19', '2002-06-14 16:02', '2002-06-14 14:02', '2000-11-13 21:21', '2000-10-05 13:00', '2000-04-07 00:00', '2000-03-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysModuleName.setRevisionsDescriptions(('Corrected the postal code in the CONTACT-INFO clause.', 'Updated CONTACT-INFO and sections 2, 6, and 7.', 'Minor change to the Applicability section.', 'Updated the CONTACT-INFO clause.\n                 Added a branch for management of Enterasys specific \n                 Internet X.509 Public Key Infrastructure Certificates.', 'Imported OBJECT-IDENTITY from SNMPv2-SMI.\n                 Removed company address from the document header.', 'Obsoleted etsysNamesMib, etsysConformance,\n                 etsysConformName, etsysConformOID.  This is the \n                 first non-experimental version of this module.', 'Fix many of the bugs in the first edit.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysModuleName.setLastUpdated('200311061515Z')
if mibBuilder.loadTexts: etsysModuleName.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysModuleName.setContactInfo('Postal:  Enterasys Networks\n                  50 Minuteman Rd.\n                  Andover, MA 01810-1008\n                  USA\n         Phone:   +1 978 684 1000\n         E-mail:  support@enterasys.com\n         WWW:     http://www.enterasys.com')
if mibBuilder.loadTexts: etsysModuleName.setDescription("This MIB module defines a portion of the SNMP enterprise\n         MIBs under Enterasys Networks enterprise OID.\n\n         This module embodies the top level hierarchy of all\n         OIDs, MIBs, AGENT-CAPABILITIES statements, and X.509\n         PKI certificates for Enterasys Networks' products.\n\n         This leaf lexicographically falls under the etsysMibs branch\n         of the enterasys enterprise tree.")
enterasys = ObjectIdentity((1, 3, 6, 1, 4, 1, 5624))
if mibBuilder.loadTexts: enterasys.setStatus('current')
if mibBuilder.loadTexts: enterasys.setDescription('Global definition of the enterasys enterprise branch\n         as provided by the Internet Assigned Numbers Authority\n         (IANA).')
etsysMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1))
etsysOids = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 2))
etsysAgentCaps = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 3))
etsysX509Pki = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 509))
etsysModules = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2))
etsysNamesMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 1))
if mibBuilder.loadTexts: etsysNamesMib.setStatus('obsolete')
if mibBuilder.loadTexts: etsysNamesMib.setDescription('Obsolete.')
etsysConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 3))
if mibBuilder.loadTexts: etsysConformance.setStatus('obsolete')
if mibBuilder.loadTexts: etsysConformance.setDescription('Obsolete.')
etsysConformName = ObjectIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 3, 1))
if mibBuilder.loadTexts: etsysConformName.setStatus('obsolete')
if mibBuilder.loadTexts: etsysConformName.setDescription('Obsolete')
etsysConformOID = ObjectIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 3, 2))
if mibBuilder.loadTexts: etsysConformOID.setStatus('obsolete')
if mibBuilder.loadTexts: etsysConformOID.setDescription('Obsolete')
mibBuilder.exportSymbols("ENTERASYS-MIB-NAMES", etsysModules=etsysModules, etsysConformance=etsysConformance, etsysConformName=etsysConformName, etsysNamesMib=etsysNamesMib, etsysOids=etsysOids, PYSNMP_MODULE_ID=etsysModuleName, etsysConformOID=etsysConformOID, etsysMibs=etsysMibs, etsysX509Pki=etsysX509Pki, enterasys=enterasys, etsysModuleName=etsysModuleName, etsysAgentCaps=etsysAgentCaps)
