#
# PySNMP MIB module RADLAN-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-LLDP-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:01:05 2022
# On host fv-az42-349 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
TruthValue, = mibBuilder.importSymbols("RADLAN-SNMPv2", "TruthValue")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, Gauge32, NotificationType, Counter32, Counter64, TimeTicks, IpAddress, MibIdentifier, ObjectIdentity, iso, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "Gauge32", "NotificationType", "Counter32", "Counter64", "TimeTicks", "IpAddress", "MibIdentifier", "ObjectIdentity", "iso", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
