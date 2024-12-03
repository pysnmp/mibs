#
# PySNMP MIB module RADLAN-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-LLDP-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 10:10:54 2024
# On host fv-az575-513 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
TruthValue, = mibBuilder.importSymbols("RADLAN-SNMPv2", "TruthValue")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, Counter32, IpAddress, iso, ObjectIdentity, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, MibIdentifier, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter32", "IpAddress", "iso", "ObjectIdentity", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "MibIdentifier", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("RADLAN-LLDP-MIB", rlLldp=rlLldp, rlLldpEnabled=rlLldpEnabled, PYSNMP_MODULE_ID=rlLldp)
