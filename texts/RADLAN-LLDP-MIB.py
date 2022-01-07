#
# PySNMP MIB module RADLAN-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-LLDP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:17:48 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
TruthValue, = mibBuilder.importSymbols("RADLAN-SNMPv2", "TruthValue")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Unsigned32, MibIdentifier, Counter64, Gauge32, Bits, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Counter64", "Gauge32", "Bits", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlLldp = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 110))
rlLldp.setRevisions(('2005-06-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlLldp.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlLldp.setLastUpdated('200506200000Z')
if mibBuilder.loadTexts: rlLldp.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlLldp.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlLldp.setDescription('This private MIB module adds MIBs to LLDP (Link Layer Discovery Protocol).')
rlLldpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 110, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpEnabled.setStatus('current')
if mibBuilder.loadTexts: rlLldpEnabled.setDescription("Setting this variable to 'true' will globally enable the LLDP feature\n             (both transmit and receive functionalities). Setting this variable\n             to 'false' will globally disable the LLDP feature. Thus, the\n             administratively desired status of a local port is determined by\n             both this variable and the MIB lldpPortConfigAdminStatus.")
mibBuilder.exportSymbols("RADLAN-LLDP-MIB", rlLldpEnabled=rlLldpEnabled, PYSNMP_MODULE_ID=rlLldp, rlLldp=rlLldp)
